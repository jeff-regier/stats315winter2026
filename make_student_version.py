#!/usr/bin/env python3
"""Release tool for homework assignments.

Validates and prepares Jupyter notebooks for student release by:
- Checking problem structure (prompt, solution, visible tests, hidden tests)
- Running ruff linting
- Executing notebooks to verify solutions pass
- Stripping solutions and hidden tests for student versions
"""

import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated

import typer

app = typer.Typer(
    help="Validate and release homework assignments.",
    add_completion=False,
)


@dataclass
class Problem:
    """Represents a homework problem with its components.

    Expected structure (otter-grader style):
    1. Prompt cell (markdown) - contains problem description
    2. Solution cell (code) - contains solution code, NO tests
    3. Test cell (code) - contains visible and hidden tests, NO solution markers
    """

    number: int
    title: str
    prompt_cell_idx: int
    solution_cell_idx: int = -1
    test_cell_idx: int = -1
    # Track validation errors for this problem
    errors: list[str] = field(default_factory=list)

    @property
    def has_prompt(self) -> bool:
        return self.prompt_cell_idx >= 0

    @property
    def has_solution(self) -> bool:
        return self.solution_cell_idx >= 0

    @property
    def has_tests(self) -> bool:
        return self.test_cell_idx >= 0

    @property
    def is_complete(self) -> bool:
        return (
            self.has_prompt and self.has_solution and self.has_tests and not self.errors
        )


@dataclass
class ValidationResult:
    """Result of validating a notebook."""

    notebook_path: Path
    problems: list[Problem] = field(default_factory=list)
    ruff_errors: list[str] = field(default_factory=list)
    execution_errors: list[str] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return (
            all(p.is_complete for p in self.problems)
            and not self.ruff_errors
            and not self.execution_errors
        )


def get_cell_source(cell: dict) -> str:
    """Get cell source as a string."""
    source = cell.get("source", [])
    if isinstance(source, list):
        return "".join(source)
    return source


def has_solution_marker(source: str) -> bool:
    """Check if source contains solution markers."""
    return "# BEGIN SOLUTION" in source or "# SOLUTION" in source


def has_hidden_tests(source: str) -> bool:
    """Check if source contains hidden test markers."""
    return "# BEGIN HIDDEN TESTS" in source


def has_visible_assert(source: str) -> bool:
    """Check if source has assert statements outside hidden test blocks."""
    if "assert " not in source:
        return False
    in_hidden = False
    for line in source.split("\n"):
        stripped = line.strip()
        if stripped == "# BEGIN HIDDEN TESTS":
            in_hidden = True
        elif stripped == "# END HIDDEN TESTS":
            in_hidden = False
        elif "assert " in line and not in_hidden:
            return True
    return False


def has_any_assert(source: str) -> bool:
    """Check if source has any assert statements (visible or hidden)."""
    return "assert " in source


# Pattern to match problem headers like:
#   "### Problem 1:" or "## (10 pts) Problem 2:"
#   "#### **Problem 3:**" or "#### **(10 pts) Problem 4:**"
PROBLEM_PATTERN = re.compile(
    r"^#{2,4}\s*\*{0,2}(?:\([^)]+\)\s*)?\*{0,2}\s*Problem\s+(\d+)[:\s*]+(.+)$",
    re.MULTILINE,
)


def find_problems(nb: dict) -> list[Problem]:
    """Find all problems in a notebook and validate their structure.

    Expected structure for each problem:
    1. Prompt cell (markdown) - contains "Problem N: title"
    2. Solution cell (code) - contains solution markers, NO asserts
    3. Test cell (code) - contains asserts (visible + hidden), NO solution markers
    """
    problems: list[Problem] = []
    cells = nb.get("cells", [])

    # First pass: find all problem prompt cells
    prompt_indices: list[tuple[int, int, str]] = []  # (cell_idx, problem_num, title)
    for idx, cell in enumerate(cells):
        if cell.get("cell_type") == "markdown":
            source = get_cell_source(cell)
            match = PROBLEM_PATTERN.search(source)
            if match:
                prompt_indices.append(
                    (idx, int(match.group(1)), match.group(2).strip())
                )

    # Second pass: validate structure for each problem
    for i, (prompt_idx, problem_num, title) in enumerate(prompt_indices):
        problem = Problem(
            number=problem_num,
            title=title,
            prompt_cell_idx=prompt_idx,
        )

        # Determine the range of cells for this problem
        next_prompt_idx = (
            prompt_indices[i + 1][0] if i + 1 < len(prompt_indices) else len(cells)
        )

        # Look for solution cell and test cell in the cells after the prompt
        solution_found = False
        test_found = False

        for idx in range(prompt_idx + 1, next_prompt_idx):
            cell = cells[idx]
            if cell.get("cell_type") != "code":
                continue

            source = get_cell_source(cell)
            cell_has_solution = has_solution_marker(source)
            cell_has_assert = has_any_assert(source)
            cell_has_hidden = has_hidden_tests(source)

            if cell_has_solution and not solution_found:
                # This is the solution cell
                problem.solution_cell_idx = idx
                solution_found = True

                # Validate: solution cell should NOT have asserts
                if cell_has_assert:
                    problem.errors.append(
                        f"Solution cell (cell {idx}) contains assert statements - "
                        "tests should be in a separate cell"
                    )

            elif cell_has_assert and solution_found and not test_found:
                # This is the test cell
                problem.test_cell_idx = idx
                test_found = True

                # Validate: test cell should NOT have solution markers
                if cell_has_solution:
                    problem.errors.append(
                        f"Test cell (cell {idx}) contains solution markers - "
                        "solution should be in the previous cell"
                    )

                # Validate: test cell should have both visible and hidden tests
                if not has_visible_assert(source):
                    problem.errors.append(
                        f"Test cell (cell {idx}) missing visible tests"
                    )
                if not cell_has_hidden:
                    problem.errors.append(
                        f"Test cell (cell {idx}) missing hidden tests"
                    )

                # Validate: test cell should start with "# Test assertions"
                first_line = source.split("\n")[0].strip() if source else ""
                if first_line != "# Test assertions":
                    problem.errors.append(
                        f"Test cell (cell {idx}) must start with '# Test assertions'"
                    )

                # Validate: test cell should be the last code cell before next problem
                # (i.e., followed by markdown or end of problem section)
                next_cell_idx = idx + 1
                if next_cell_idx < next_prompt_idx:
                    next_cell = cells[next_cell_idx]
                    if next_cell.get("cell_type") == "code":
                        problem.errors.append(
                            f"Test cell (cell {idx}) should be followed by a markdown "
                            f"cell, not another code cell (cell {next_cell_idx})"
                        )

        problems.append(problem)

    return problems


def extract_code_cells(nb: dict) -> str:
    """Extract all code from code cells for ruff checking."""
    code_parts = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            source = get_cell_source(cell)
            code_parts.append(source)
    return "\n\n".join(code_parts)


def run_ruff_check(notebook_path: Path) -> list[str]:
    """Run ruff on notebook code and return any errors."""
    try:
        result = subprocess.run(
            ["ruff", "check", str(notebook_path), "--output-format=concise"],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    except FileNotFoundError:
        return ["ruff not found - install with: pip install ruff"]
    except subprocess.TimeoutExpired:
        return ["ruff check timed out"]
    if result.returncode != 0:
        return [
            line
            for line in result.stdout.strip().split("\n")
            if line and not line.startswith("Found")
        ]
    return []


def run_notebook(notebook_path: Path) -> list[str]:
    """Execute a notebook and return any assertion errors.

    Uses --allow-errors since educational notebooks often have intentional
    error cells to demonstrate exceptions. Only fails on assertion errors
    which indicate test failures.
    """
    try:
        result = subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "--allow-errors",
                "--inplace",
                str(notebook_path),
            ],
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
    except FileNotFoundError:
        return ["jupyter not found - install with: pip install jupyter"]
    except subprocess.TimeoutExpired:
        return ["Notebook execution timed out (>5 minutes)"]
    if result.returncode != 0:
        error_output = result.stderr.strip()
        if "AssertionError" in error_output:
            lines = error_output.split("\n")
            errors = [line for line in lines if "AssertionError" in line]
            return errors[:5] if errors else ["Assertion failed"]
    return []


def validate_notebook(
    notebook_path: Path,
    check_ruff: bool = True,
    check_execution: bool = True,
) -> ValidationResult:
    """Validate a notebook for completeness."""
    with notebook_path.open() as f:
        nb = json.load(f)

    problems = find_problems(nb)
    ruff_errors = run_ruff_check(notebook_path) if check_ruff else []
    execution_errors = run_notebook(notebook_path) if check_execution else []

    return ValidationResult(
        notebook_path=notebook_path,
        problems=problems,
        ruff_errors=ruff_errors,
        execution_errors=execution_errors,
    )


def strip_solutions_and_hidden_tests(source_lines: list[str]) -> list[str]:
    """Remove solution code and hidden tests from cell source lines."""
    result = []
    in_solution = False
    in_hidden_tests = False

    for line in source_lines:
        stripped = line.rstrip("\n").strip()

        # Handle solution markers
        if stripped == "# BEGIN SOLUTION":
            in_solution = True
            indent = len(line) - len(line.lstrip())
            result.append(" " * indent + "# your code here\n")
            continue
        if stripped == "# END SOLUTION":
            in_solution = False
            continue

        # Handle hidden test markers
        if stripped == "# BEGIN HIDDEN TESTS":
            in_hidden_tests = True
            continue
        if stripped == "# END HIDDEN TESTS":
            in_hidden_tests = False
            continue

        # Skip lines inside solution or hidden test blocks
        if in_solution or in_hidden_tests:
            continue

        # Handle inline solution marker (must end with # SOLUTION)
        if line.rstrip().endswith("# SOLUTION"):
            indent = len(line) - len(line.lstrip())
            # Extract variable name if there's an assignment (not ==, !=, <=, >=)
            code_part = line.split("# SOLUTION")[0].rstrip()
            # Match assignment: var = value (but not ==, !=, <=, >=)
            assign_match = re.match(r"^(\s*)([^=!<>]+)\s*=[^=]", code_part)
            if assign_match:
                var_name = assign_match.group(2).rstrip()
                result.append(" " * indent + var_name + " = ...  # your code here\n")
            else:
                result.append(" " * indent + "# your code here\n")
            continue

        result.append(line)

    # Remove trailing empty lines
    while result and result[-1].strip() == "":
        result.pop()

    # Remove trailing newline from last line
    if result and result[-1].endswith("\n"):
        result[-1] = result[-1][:-1]

    return result


def is_test_header_comment(line: str) -> bool:
    """Check if a line is a test section header comment."""
    stripped = line.strip().lower()
    return stripped.startswith("# test") and not stripped.startswith("# testing")


def split_solution_and_tests(source_lines: list[str]) -> tuple[list[str], list[str]]:
    """Split a cell's source into solution code and test code.

    Returns (solution_lines, test_lines).
    """
    solution_lines: list[str] = []
    test_lines: list[str] = []

    in_solution = False
    found_test_start = False

    for line in source_lines:
        stripped = line.rstrip("\n").strip()

        # Track solution blocks
        if stripped == "# BEGIN SOLUTION":
            in_solution = True
        elif stripped == "# END SOLUTION":
            in_solution = False

        # Track hidden test blocks
        if stripped in {"# BEGIN HIDDEN TESTS", "# END HIDDEN TESTS"}:
            pass

        # Check if this line starts the test section
        is_assert_line = "assert " in line and not in_solution
        is_hidden_marker = stripped == "# BEGIN HIDDEN TESTS"
        is_test_comment = is_test_header_comment(line) and not in_solution

        if (
            is_assert_line or is_hidden_marker or is_test_comment
        ) and not found_test_start:
            found_test_start = True

        # Route line to appropriate section
        if found_test_start:
            test_lines.append(line)
        else:
            solution_lines.append(line)

    # Clean up trailing empty lines from solution
    while solution_lines and solution_lines[-1].strip() == "":
        solution_lines.pop()

    # Add newline at end of solution if needed
    if solution_lines and not solution_lines[-1].endswith("\n"):
        solution_lines[-1] += "\n"

    return solution_lines, test_lines


def fix_notebook_structure(notebook_path: Path) -> tuple[int, int]:
    """Fix notebook structure by splitting combined solution/test cells.

    Returns (cells_split, cells_unchanged).
    """
    with notebook_path.open() as f:
        nb = json.load(f)

    new_cells = []
    cells_split = 0
    cells_unchanged = 0

    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            new_cells.append(cell)
            continue

        source = cell.get("source", [])
        if isinstance(source, str):
            source = source.split("\n")
            source = [line + "\n" for line in source[:-1]] + [source[-1]]

        source_text = "".join(source)
        cell_has_solution = has_solution_marker(source_text)
        cell_has_assert = has_any_assert(source_text)

        # If cell has both solution and tests, split it
        if cell_has_solution and cell_has_assert:
            solution_lines, test_lines = split_solution_and_tests(source)

            if solution_lines and test_lines:
                # Create solution cell
                solution_cell = cell.copy()
                solution_cell["source"] = solution_lines
                solution_cell["outputs"] = []
                solution_cell["execution_count"] = None
                new_cells.append(solution_cell)

                # Create test cell
                test_cell = {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": test_lines,
                }
                new_cells.append(test_cell)
                cells_split += 1
            else:
                # Couldn't split properly, keep original
                new_cells.append(cell)
                cells_unchanged += 1
        else:
            new_cells.append(cell)
            cells_unchanged += 1

    nb["cells"] = new_cells

    with notebook_path.open("w") as f:
        json.dump(nb, f, indent=1)

    return cells_split, cells_unchanged


def process_notebook(input_path: Path, output_dir: Path) -> tuple[Path, int, int]:
    """Process a notebook and write the student version."""
    with input_path.open() as f:
        nb = json.load(f)

    solutions_stripped = 0
    hidden_tests_stripped = 0

    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            # Clear outputs and execution count for student version
            cell["outputs"] = []
            cell["execution_count"] = None

            source = cell.get("source", [])
            if isinstance(source, str):
                source = source.split("\n")
                source = [line + "\n" for line in source[:-1]] + [source[-1]]

            source_text = "".join(source)
            has_solution = (
                "# BEGIN SOLUTION" in source_text or "# SOLUTION" in source_text
            )
            has_hidden = "# BEGIN HIDDEN TESTS" in source_text

            if has_solution or has_hidden:
                cell["source"] = strip_solutions_and_hidden_tests(source)
                if has_solution:
                    solutions_stripped += 1
                if has_hidden:
                    hidden_tests_stripped += 1

    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / input_path.name

    with output_file.open("w") as f:
        json.dump(nb, f, indent=1)

    return output_file, solutions_stripped, hidden_tests_stripped


@app.command()
def check(
    notebooks: Annotated[
        list[Path],
        typer.Argument(
            help="Notebook files to validate",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    skip_ruff: Annotated[
        bool,
        typer.Option("--skip-ruff", help="Skip ruff linting check"),
    ] = False,
    skip_execution: Annotated[
        bool,
        typer.Option("--skip-execution", help="Skip notebook execution check"),
    ] = False,
) -> None:
    """Validate notebooks: problems, ruff, and execution."""
    all_valid = True

    for notebook_path in notebooks:
        print(f"\n{notebook_path}")
        print("=" * 60)

        result = validate_notebook(
            notebook_path,
            check_ruff=not skip_ruff,
            check_execution=not skip_execution,
        )

        if not result.problems:
            print("  No problems found in notebook")
            all_valid = False
            continue

        for problem in result.problems:
            print(f"  Problem {problem.number}: {problem.title}")

            missing = []
            if not problem.has_prompt:
                missing.append("prompt cell")
            if not problem.has_solution:
                missing.append("solution cell")
            if not problem.has_tests:
                missing.append("test cell")

            if missing:
                print(f"    MISSING: {', '.join(missing)}")
                all_valid = False

            if problem.errors:
                for error in problem.errors:
                    print(f"    ERROR: {error}")
                all_valid = False

            if not missing and not problem.errors:
                print("    OK")

        if result.ruff_errors:
            print("\n  Ruff errors:")
            for error in result.ruff_errors[:10]:
                print(f"    {error}")
            if len(result.ruff_errors) > 10:
                print(f"    ... and {len(result.ruff_errors) - 10} more")
            all_valid = False

        if result.execution_errors:
            print("\n  Execution errors:")
            for error in result.execution_errors[:5]:
                print(f"    {error}")
            all_valid = False

        if not result.ruff_errors and not result.execution_errors:
            print("\n  Ruff: OK")
            print("  Execution: OK")

    print()
    if all_valid:
        print("All notebooks valid!")
    else:
        print("Some notebooks have issues.")
        raise typer.Exit(1)


@app.command()
def release(
    notebooks: Annotated[
        list[Path],
        typer.Argument(
            help="Notebook files to release",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    output_dir: Annotated[
        Path,
        typer.Option(
            "--output-dir",
            "-o",
            help="Output directory for student versions",
        ),
    ] = Path("student"),
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="Show what would be done without writing files",
        ),
    ] = False,
    skip_check: Annotated[
        bool,
        typer.Option(
            "--skip-check",
            help="Skip validation before releasing (not recommended)",
        ),
    ] = False,
) -> None:
    """Validate and release notebooks for students.

    Runs validation (problems, ruff, execution) then creates student versions
    with solutions and hidden tests removed. Original files are never modified.
    """
    # Run validation first unless skipped
    if not skip_check:
        print("Validating notebooks...")
        all_valid = True
        for notebook_path in notebooks:
            result = validate_notebook(
                notebook_path, check_ruff=True, check_execution=True
            )

            if not result.problems:
                print(f"  {notebook_path}: No problems found")
                all_valid = False
                continue

            incomplete = [p for p in result.problems if not p.is_complete]
            if incomplete:
                print(f"  {notebook_path}: {len(incomplete)} incomplete problem(s)")
                for p in incomplete:
                    issues = []
                    if not p.has_solution:
                        issues.append("missing solution cell")
                    if not p.has_tests:
                        issues.append("missing test cell")
                    issues.extend(p.errors)
                    print(f"    Problem {p.number}: {'; '.join(issues)}")
                all_valid = False

            if result.ruff_errors:
                print(f"  {notebook_path}: {len(result.ruff_errors)} ruff error(s)")
                all_valid = False

            if result.execution_errors:
                print(f"  {notebook_path}: execution failed")
                for err in result.execution_errors[:3]:
                    print(f"    {err}")
                all_valid = False

        if not all_valid:
            print("\nValidation failed. Fix issues or use --skip-check to bypass.")
            raise typer.Exit(1)

        print("All notebooks valid.\n")

    # Proceed with stripping
    if not dry_run:
        output_dir.mkdir(exist_ok=True)

    total_solutions = 0
    total_hidden = 0

    for notebook in notebooks:
        if dry_run:
            with notebook.open() as f:
                nb = json.load(f)
            sol_count = sum(
                1
                for c in nb["cells"]
                if c.get("cell_type") == "code"
                and (
                    "# BEGIN SOLUTION" in get_cell_source(c)
                    or "# SOLUTION" in get_cell_source(c)
                )
            )
            hidden_count = sum(
                1
                for c in nb["cells"]
                if c.get("cell_type") == "code"
                and "# BEGIN HIDDEN TESTS" in get_cell_source(c)
            )
            output_file = output_dir / notebook.name
            print(
                f"[dry-run] {notebook} -> {output_file} "
                f"({sol_count} solutions, {hidden_count} hidden tests)"
            )
        else:
            output_file, sol_count, hidden_count = process_notebook(
                notebook, output_dir
            )
            print(
                f"{notebook} -> {output_file} "
                f"({sol_count} solutions, {hidden_count} hidden tests stripped)"
            )

        total_solutions += sol_count
        total_hidden += hidden_count

    suffix = " [dry-run]" if dry_run else ""
    print(
        f"\nProcessed {len(notebooks)} notebook(s): "
        f"{total_solutions} solution(s), {total_hidden} hidden test(s){suffix}"
    )


@app.command("fix-structure")
def fix_structure(
    notebooks: Annotated[
        list[Path],
        typer.Argument(
            help="Notebook files to fix",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    dry_run: Annotated[
        bool,
        typer.Option(
            "--dry-run",
            "-n",
            help="Show what would be done without modifying files",
        ),
    ] = False,
) -> None:
    """Fix notebook structure by splitting combined solution/test cells.

    For cells that contain both solution markers and assert statements,
    splits them into separate cells:
    1. Solution cell (code with solution markers)
    2. Test cell (asserts and hidden tests)

    This converts notebooks to the otter-grader style structure.
    """
    total_split = 0

    for notebook_path in notebooks:
        if dry_run:
            with notebook_path.open() as f:
                nb = json.load(f)

            split_count = 0
            for cell in nb["cells"]:
                if cell.get("cell_type") != "code":
                    continue
                source_text = get_cell_source(cell)
                if has_solution_marker(source_text) and has_any_assert(source_text):
                    split_count += 1

            print(f"[dry-run] {notebook_path}: would split {split_count} cell(s)")
            total_split += split_count
        else:
            cells_split, _ = fix_notebook_structure(notebook_path)
            print(f"{notebook_path}: split {cells_split} cell(s)")
            total_split += cells_split

    suffix = " [dry-run]" if dry_run else ""
    print(f"\nTotal: {total_split} cell(s) split{suffix}")


if __name__ == "__main__":
    app()
