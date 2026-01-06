---
## Critique: DATASCI 503, Group Work 10: Stochastic Gradient Descent for Loss Functions

### Issues Requiring Review

#### 1. Title Mismatch: "Stochastic" vs "Minibatch" Gradient Descent
**Location:** Cell 0 (title)
**Description:** The assignment title mentions "Stochastic Gradient Descent" but Problem 5 implements minibatch gradient descent. True SGD uses batch_size=1.
**Why it needs review:** This is a naming/pedagogical decision. Options: (1) rename to "Gradient Descent Methods for Loss Functions", (2) add a problem specifically implementing SGD with batch_size=1, or (3) keep as-is if the term is used loosely in the course.

#### 2. Missing Mathematical Derivation for Gradients
**Location:** Problems 1-3
**Description:** Students are expected to implement gradient descent but the gradients are not derived or provided explicitly. The gradient formulas appear only in solution comments (hidden from students).
**Why it needs review:** Pedagogical decision on whether students should derive gradients themselves or be given the formulas. If derivation is expected, this may be intentional; if not, formulas should be added to the problem statements.

#### 3. Inconsistent Convergence Criteria Across Problems
**Location:** Problems 1-5
**Description:** Different problems use different convergence criteria: Problem 1 uses parameter change only, Problem 2 uses L2 norm of parameter change, Problems 3-4 use both parameter AND loss change, Problem 5 uses L1 norm of parameter change only.
**Why it needs review:** May be intentional to expose students to different approaches, or may want to standardize for clarity. Requires decision on pedagogical intent.

#### 4. Convergence Condition in Problem 3: AND vs OR
**Location:** Cell 17-18
**Description:** The problem description (Cell 17) says convergence can be checked "in either of two ways" (suggesting OR), but the solution implementation requires BOTH conditions (AND).
**Why it needs review:** Need to decide if the documentation or implementation should be updated to match the other.

#### 5. No Maximum Iteration Limit
**Location:** All gradient descent implementations (Cells 7, 11, 18, 28, 41)
**Description:** None of the gradient descent functions include a maximum iteration limit. With poor learning rate choices, these functions could run indefinitely.
**Why it needs review:** Decision needed on whether to add a max_iterations parameter (with default like 10000) as a safety measure, or leave as-is for simplicity.

#### 6. Test Cells Depend on Prior Cell Execution Order
**Location:** Cells 30-33, 42-45
**Description:** Test cells for Problems 4 and 5 rely on variables defined in earlier cells (e.g., `X_train_scaled`, `lr_multi`, `sklearn_train_loss`, `X_val_with_intercept`). Running cells out of order causes confusing errors.
**Why it needs review:** Decision needed on whether to make test cells more self-contained, add execution order warnings, or keep as-is (standard notebook workflow).

---
