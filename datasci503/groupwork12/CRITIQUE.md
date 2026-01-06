---
## Critique: DATASCI 503, Group Work 12: Fashion MNIST with Regularization

### Issues Requiring Review

#### 1. Problem 9 Test Assertions Do Not Verify Implicit Regularization Effect
**Location:** Problem 9, test cell (cell-43)
**Description:** The test assertions for Problem 9 only check that training occurred (loss decreased) and that 50 epochs ran. They do not verify that implicit regularization actually reduced overfitting compared to Problem 2.
**Why it needs review:** The pedagogical goal is for students to demonstrate that implicit regularization reduces overfitting. Adding an assertion comparing the validation-training loss gap to the overfitting model would make this explicit, but the instructor may prefer leaving it open-ended for learning purposes.

#### 2. Problem 1 Hint Potentially Gives Away Solution
**Location:** Problem 1 description (cell-7)
**Description:** The hint explicitly states "Use a very small hidden layer (e.g., 2 neurons)" which essentially provides the exact solution approach.
**Why it needs review:** The instructor should decide whether this level of scaffolding is appropriate for the course level, or if a more general hint about model capacity would better support learning.

#### 3. Problem 2 Does Not Specify Clear Success Criteria for Overfitting
**Location:** Problem 2 description (cell-11)
**Description:** The problem says validation loss should "begin increasing" but does not specify how much or when.
**Why it needs review:** Adding specific guidance (e.g., "validation loss should reach its minimum within the first 30-40 epochs and then increase by at least 0.1") may help students but could also reduce the exploratory nature of the assignment.

#### 4. Problem 10 Free-Response Structure
**Location:** Problem 10 (cells 47-48)
**Description:** The question "Which model would you choose for deployment and why?" appears in a separate markdown cell from the solution markers, creating an awkward structure.
**Why it needs review:** The instructor should decide whether to combine the question with the solution markers in a single cell or restructure using a subproblem header format.

#### 5. Inconsistent Dropout Placement in Solutions
**Location:** Problems 6, 7, 8 solutions
**Description:** The solutions only add dropout after the first hidden layer, but not after the second. This inconsistency may confuse students about where dropout should be placed.
**Why it needs review:** The instructor should decide whether to add dropout after both hidden layers for consistency, or add an explanatory note about common dropout placement strategies.

#### 6. Problem 6 Hint Discrepancy with Solution
**Location:** Problem 6 description (cell-28)
**Description:** The hint suggests "p=0.5 or higher" but the solution uses p=0.7. The hint could mention that higher dropout rates provide stronger regularization.
**Why it needs review:** The instructor should decide whether to align the hint with the solution value or explain the trade-offs of different dropout rates.

#### 7. Confusion Matrix Labels Use Numeric Values
**Location:** Problem 10 solution (cell-46)
**Description:** The confusion matrices use numeric labels (0-9) rather than class names (T-shirt, Trouser, etc.), making interpretation harder.
**Why it needs review:** Adding class name labels would improve readability but may add complexity to the solution code. The instructor should decide if this educational benefit outweighs the added code complexity.

---
