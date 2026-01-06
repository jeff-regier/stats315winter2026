# Winter 2026 Assignments

Course materials for DATASCI 315 and DATASCI 503, including homework and groupwork Jupyter notebook assignments.

## Repository Structure

```
datasci315/
  homework1/
    homework1.ipynb      # Instructor version (with solutions)
    student/
      homework1.ipynb    # Student version (solutions stripped)
  groupwork1/
    ...
datasci503/
  ...
```

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Install it first:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then install dependencies:

```bash
uv sync
```

This creates a `.venv` directory with all required packages (PyTorch, scikit-learn, pandas, etc.).

## Running Notebooks

Always use `uv run` to ensure you're using the correct environment:

```bash
uv run jupyter lab
```

Or activate the environment first:

```bash
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

jupyter lab
```

## Creating Student Versions

Use `make_student_version.py` to validate an assignment and generate the student version:

```bash
uv run python make_student_version.py path/to/assignment.ipynb
```

This script:
1. **Validates structure** - Checks that each problem has a prompt, solution, and test cell
2. **Runs ruff** - Checks for code style issues
3. **Executes the notebook** - Verifies all solutions pass their tests
4. **Strips solutions** - Creates a student version in the `student/` subdirectory

Example:
```bash
uv run python make_student_version.py datasci315/homework3/homework3.ipynb
# Creates: datasci315/homework3/student/homework3.ipynb
```

## Linting

[Ruff](https://docs.astral.sh/ruff/) checks code style. Run it manually:

```bash
# Check for issues
uv run ruff check path/to/notebook.ipynb

# Auto-fix issues
uv run ruff check --fix path/to/notebook.ipynb

# Format code
uv run ruff format path/to/notebook.ipynb
```

## Assignment Conventions

### Problem Headers

Use markdown headers (no bold, no point values in header):

```markdown
### Problem 1: Title Here
```

### Solution Markers

**Code solutions** (in code cells):
```python
# BEGIN SOLUTION
answer = compute_result()
# END SOLUTION
```

**Inline solutions** (single line):
```python
result = 42  # SOLUTION
```

**Free-response solutions** (in markdown cells):
```markdown
> BEGIN SOLUTION

Your explanation here.

> END SOLUTION
```

### Test Cell Structure

Test cells must be **separate from solution cells** and follow this format:

```python
# Test assertions
assert result == expected, "Descriptive error message"
print("All tests passed!")

# BEGIN HIDDEN TESTS
assert edge_case == expected, "Hidden test description"
# END HIDDEN TESTS
```

### Example Problem Structure

```
Cell 1 (Markdown):
  ### Problem 1: Calculate Mean
  Write a function that calculates the mean of a list.

Cell 2 (Code):
  # BEGIN SOLUTION
  def mean(values):
      return sum(values) / len(values)
  # END SOLUTION

Cell 3 (Code):
  # Test assertions
  assert mean([1, 2, 3]) == 2.0, "Mean of [1,2,3] should be 2.0"
  print("All tests passed!")

  # BEGIN HIDDEN TESTS
  assert mean([0]) == 0.0
  # END HIDDEN TESTS
```

## Common Issues

**"No problems found"** - Check that problem headers match the format `### Problem N: Title`

**Ruff errors** - Run `uv run ruff check --fix` to auto-fix most issues

**Execution errors** - Open the notebook and run cells manually to debug

**Missing test cell** - Each code problem needs a separate cell with `# Test assertions` as the first line
