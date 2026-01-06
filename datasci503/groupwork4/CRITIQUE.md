---
## Critique: DATASCI 503, Group Work 4: Linear and Quadratic Discriminant Analysis

### Issues Requiring Review

#### 1. Missing Data Path Configuration for Problem 10
**Location:** Cell 43 (Problem 10: QDA on NHANES Dataset)
**Description:** The solution hardcodes `data_path = "../datasets/NHANES/"` but students receive no guidance on where data should be located or how to access it. The problem statement provides no starter code or data loading instructions.
**Why it needs review:** This is a data handling decision. Options include: (1) adding starter code that loads the data for students, (2) providing clear instructions with the data path, or (3) including a data loading cell before the problem similar to how the breast cancer dataset is loaded in Problem 8. The instructor needs to decide how the NHANES data will be distributed to students.

#### 2. Problem 10-11 Structure - Missing Starter Code and Variable Names
**Location:** Cells 42-47 (Problems 10 and 11)
**Description:** Problems 10 and 11 have their entire solutions in single cells, including data loading, preprocessing, model fitting, and visualization. The test cells reference variables (`qda`, `y_pred`, `y_test`, `X_scaled`, `X_train`, `X_test`, `xx`, `yy`, `Z`) that students must create with exact names, but no starter code skeleton is provided.
**Why it needs review:** This is a pedagogical choice about how much scaffolding to provide. Earlier problems in the notebook provide function signatures as starter code, but these problems do not. The instructor should decide whether to: (1) add starter code with variable names and structure, (2) break into smaller testable components, or (3) keep as open-ended problems where students must determine the structure themselves.

#### 3. Weak Visible Test May Give Away Solution Structure
**Location:** Cell 18 (Problem 2 tests)
**Description:** Test case 2 uses `expected4 = 2` which is a suspiciously round number that could be reverse-engineered. With identity covariance, zero prior log, and mu=[2,2], the answer is simply x.dot(mu) - 0.5*mu.dot(mu) = 6 - 4 = 2.
**Why it needs review:** This is a pedagogical choice about test design. The instructor may want to keep simple test cases for debugging purposes, or may prefer to use less obvious expected values to prevent reverse-engineering.

#### 4. Free Response Problems Lack Rubric Guidance
**Location:** Cells 14-15 (Problem 1), 29-30 (Problem 6), 40-41 (Problem 9)
**Description:** Free response problems ask for definitions and parameter counts but provide no guidance on expected depth or format of answers.
**Why it needs review:** The instructor should decide whether to add expectations like "Your answer should include the mathematical formula and a brief explanation of each term" or "Express your answer as a formula in terms of k and d."

#### 5. Problem 10 Missing Specific Requirements
**Location:** Cell 42
**Description:** The problem statement mentions to "scale your data and split it into train and test sets" but does not specify the test size, random state, or whether to print accuracy.
**Why it needs review:** The instructor should decide whether to add specific requirements (e.g., "Use a test size of 0.2 and random_state=42 for reproducibility. Report the test accuracy.") or leave it open-ended for students to make their own choices.

---
