---
## Critique: DATASCI 503, Group Work 11: Building and Tuning Neural Networks in PyTorch

### Issues Requiring Review

#### 1. Data File Path Not Documented
**Location:** cell-18
**Description:** The code loads from `"data/higgs.csv"` but there's no indication to students where this file comes from or how to obtain it.
**Why it needs review:** This is a content decision about whether to add download instructions, provide the file, or add a note about its location.

#### 2. Problem 5b Test Loss vs Validation Loss Confusion
**Location:** cell-35
**Description:** The problem asks students to "record the final validation loss" but then asks to "print out the test loss of the best performing model." The solution computes test loss on `X_test` directly without using the test_loader and without proper batching for large datasets.
**Why it needs review:** This is a pedagogical decision about whether to clarify the distinction between validation and test sets, and whether to require using the test_loader for proper evaluation.

#### 3. Missing Test Cells for Problem 5b
**Location:** Problem 5b (after cell-35)
**Description:** Problem 5b has no test assertions cell verifying that students tested at least 8 model configurations and recorded results.
**Why it needs review:** Adding test coverage for this problem requires a pedagogical decision about what exactly to verify (number of configurations, result format, etc.).

#### 4. Suspiciously Low Test Loss in Solution
**Location:** cell-36
**Description:** The example solution mentions "test loss of approximately 0.0058" which is suspiciously low for cross-entropy loss on a classification task (typical values would be around 0.5-0.7).
**Why it needs review:** This value should be verified by running the notebook. If incorrect, it may confuse students about expected results.

#### 5. Problem 6 Parts Share Model Variables
**Location:** Problems 6a, 6b, 6c, 6d
**Description:** Each part reuses the variable names `model`, `criterion`, `optimizer` without clearing previous state.
**Why it needs review:** This may be intentional to show variable reuse patterns, or it could benefit from distinct variable names or comments clarifying that variables will be overwritten.

#### 6. Cross-Entropy Loss Output Dimension Explanation Missing
**Location:** Throughout (models use `output_dim=2` for binary classification)
**Description:** Students might not understand why binary classification uses 2 output neurons with CrossEntropyLoss instead of 1 output neuron with BCEWithLogitsLoss.
**Why it needs review:** Adding an explanation is a pedagogical decision about the scope of the assignment.

---
