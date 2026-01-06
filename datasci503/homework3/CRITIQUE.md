---
## Critique: DATASCI 503, Homework 3: Logistic Regression

### Issues Requiring Review

#### 1. Problem 2 Covers KNN Instead of Logistic Regression
**Location:** Problem 2 (cells 5-6)
**Description:** Problem 2 is entirely about the curse of dimensionality in K-nearest neighbors (KNN), which is unrelated to logistic regression. The assignment introduction explicitly states this covers "the mathematical foundations of logistic regression."
**Why it needs review:** This is a pedagogical content decision. The problem may be intentionally included to contrast parametric (logistic regression) vs non-parametric (KNN) methods, or it may be misplaced content. Decide whether to keep it, remove it, or replace it with a logistic regression problem.

#### 2. Problem 4 Coefficient Mismatch May Confuse Students
**Location:** Problem 4, part (c) solution (cell 10)
**Description:** The solution derives the correct relationship between binary logistic and softmax coefficients, then "verifies" with values that don't match, noting the models "differ." The problem asks students to "show the relationship," implying equivalence, but the given coefficients are intentionally mismatched.
**Why it needs review:** This could be a deliberate teaching point about how different parameterizations can yield different predictions, or it could confuse students who expect the values to work out. Consider revising the problem wording to explicitly ask students to verify whether the two models are equivalent.

#### 3. Missing Dataset Description for Applied Problems
**Location:** Before Problem 6 (cell 16)
**Description:** The assignment loads CSV files from `./data/college_train.csv` and `./data/college_test.csv` without describing the dataset, what features it contains, what "Private" means, or the source of the data.
**Why it needs review:** Adding dataset context is a content decision that affects assignment length and scope. Determine whether to add a description cell, link to documentation, or leave it minimal.

#### 4. Problem 9 Missing Conceptual Answer
**Location:** Problem 9 (cells 27-28)
**Description:** The problem asks "What happens to TPR and FPR when we increase the threshold?" but the solution only prints values without explicitly answering this conceptual question.
**Why it needs review:** Decide whether to add a free-response section asking students to explain the relationship, or add explanatory text to the solution about how increasing the threshold decreases both TPR and FPR (the model becomes more conservative).

#### 5. Problems 8-9 Use Inconsistent Methods for Computing Metrics
**Location:** Problems 8 and 9 (cells 25, 28)
**Description:** Problem 8 uses confusion matrix elements directly, while Problem 9 uses `sklearn.metrics.recall_score`. Students may be confused by the different approaches.
**Why it needs review:** This is a pedagogical choice. Using confusion matrix teaches the underlying concepts; using sklearn functions teaches practical API usage. Decide whether consistency is preferred or if showing both approaches is valuable.

#### 6. Hidden Test Thresholds May Be Too Strict
**Location:** Problems 8, 11 (cells 26, 35)
**Description:** Hidden tests require `tpr > 0.9`, `fpr < 0.15`, and `auc > 0.95`. These thresholds depend on the specific train/test split and could fail if data changes.
**Why it needs review:** Determine whether to loosen thresholds (e.g., `tpr > 0.85`, `auc > 0.90`), add a fixed random seed for reproducibility, or keep the current strict thresholds.

#### 7. Cell 13 Contains Instructor Verification Code
**Location:** Cell 13
**Description:** This cell contains code that verifies the Problem 5 calculations, but it's not part of a solution block and appears to be instructor-provided verification rather than student work.
**Why it needs review:** Decide whether to move this after the solution cell, wrap it in solution markers if students should write it, or remove it entirely to avoid confusion about what students are expected to do.

---
