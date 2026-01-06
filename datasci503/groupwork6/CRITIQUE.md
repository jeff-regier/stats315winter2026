---
## Critique: DATASCI 503, Group Work 6: Splines and GAMs

### Issues Requiring Review

#### 1. Missing Data Download Instructions for NHANES
**Location:** Problem 3 (Cells 52-54)
**Description:** The problem references local files (`data/BMX_L.xpt`, `data/DEMO_L.xpt`, `data/HDL_L.xpt`) but does not explain where students should download them from.
**Why it needs review:** This is a content decision about whether to add download instructions, provide a setup cell that automatically downloads the files, or include the files in the repository.

#### 2. Inconsistent Input Shape Documentation
**Location:** Problem 1 solution (Cell 45)
**Description:** The function docstring says `X` is a "1D array" but the solution immediately reshapes it with `X = X.reshape(-1, 1)`. The test also passes `X = x.reshape(-1, 1)` (already 2D). This inconsistency could confuse students.
**Why it needs review:** This is a pedagogical choice about how to document the expected input format and whether the function should handle both 1D and 2D inputs.

#### 3. "Think About" Questions Lack Expected Engagement
**Location:** Cells 18, 24, 32
**Description:** Three "Think About" questions are posed but there's no indication whether students should answer them, discuss with partners, or if they're rhetorical. The question about integral limits (Cell 18) is never answered anywhere.
**Why it needs review:** This is a pedagogical choice about whether to convert these to graded free-response problems, add inline answers for self-study, or leave them as discussion prompts.

#### 4. Problem 3 Lacks Intermediate Verification
**Location:** Cells 53-54
**Description:** Students must figure out variable names from external documentation, merge three datasets, rename columns, and drop NAs. If anything goes wrong, the only visible test is the final shape check.
**Why it needs review:** This is a pedagogical choice about whether to add intermediate assertions, print statements showing expected shapes after each merge, or provide the column mapping directly in the problem statement.

#### 5. Problem 5 GridSearchCV Comment Formula Clarity
**Location:** Cell 62 hidden tests
**Description:** The comment `n_spline_features = n_features * (4 + 2 - 1)  # n_knots=4, degree=2` uses a formula that may not match the sklearn documentation formula for SplineTransformer output features.
**Why it needs review:** The comment formula could be clarified or replaced with the actual sklearn formula to avoid confusion during grading or future maintenance.

#### 6. Hardcoded Y-Limits in Partial Dependence Plot
**Location:** Cell 41
**Description:** The `ax.set_ylim(-30, 30)` may clip partial dependence plots for different datasets or random seeds.
**Why it needs review:** This could be intentional to maintain consistent visualization across runs, or it may need to be removed/adjusted to accommodate different data ranges.

#### 7. Missing Random State in Problem 7 GridSearch
**Location:** Cell 69
**Description:** The gridsearch in Problem 7 doesn't set a random state, which could lead to non-reproducible results.
**Why it needs review:** This could be intentional to demonstrate real-world variability, or a random_state should be added for reproducibility in autograding.

#### 8. UCI URL Stability
**Location:** Cell 37
**Description:** The UCI ML Repository URL for breast cancer data could change over time.
**Why it needs review:** Consider whether to switch to sklearn's `load_breast_cancer()` for stability, or if using the external URL is pedagogically valuable for teaching data loading.

---
