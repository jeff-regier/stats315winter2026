---
## Critique: DATASCI 503, Group Work 8: Support Vector Machines

### Issues Requiring Review

#### 1. Variable Overwriting Creates Hidden Dependencies
**Location:** Problems 1 and 6 (cells 21 and 41)
**Description:** Problem 6 overwrites `X` and `y` with new data from `make_circles`, destroying the data from Problem 1. This means if a student runs cells out of order, they will get confusing errors.
**Why it needs review:** This is a pedagogical/design decision. Using distinct variable names like `X_blobs, y_blobs` and `X_circles, y_circles` would allow non-linear execution, but may add complexity. Alternatively, this could be intentional to teach notebook execution order.

---

#### 2. Missing Random State Specification in Problem Text
**Location:** Problems 3 and 7 (cells 28 and 44)
**Description:** The problem statements require `train_test_split` but do not specify what `random_state` to use. The solution uses `random_state=503` but this is not mentioned in the instructions.
**Why it needs review:** Either explicitly state `random_state=503` in the problem text, or remove the hidden test dependencies on exact split results. This affects reproducibility expectations.

---

#### 3. Missing Scaffolding for Problem 8
**Location:** Cell 48
**Description:** Problem 8 requires students to use `gamma=1` for the polynomial SVM to match the explicit feature mapping, but this is not explained or hinted at in the problem statement.
**Why it needs review:** Students may struggle to understand why `gamma=1` is necessary. Consider adding a hint explaining that `gamma=1` is required for the kernel to match the explicit feature mapping, or provide a link to sklearn documentation explaining kernel parameters.

---

#### 4. Problem 9 Outline Missing Critical Details
**Location:** Cell 54
**Description:** The outline mentions using `svc.decision_function` but doesn't clarify that students need to use `poly_svm` and `lin_feature_svm` (variables defined in the previous cell). Also doesn't explain what `levels=[0]` means in `plt.contour`.
**Why it needs review:** Consider being explicit about which variable names to use, and briefly explain that `levels=[0]` plots the decision boundary where the decision function equals zero.

---

#### 5. GitHub Link May Become Stale
**Location:** Cell 17
**Description:** The notebook links to an external GitHub file for attribution. This link may become stale over time.
**Why it needs review:** Consider archiving the content, removing the link, or using a more permanent reference. This is a content stability decision.

---

#### 6. Non-Standard Terminology
**Location:** Cell 20
**Description:** The term "quasi-linearly separable" is used, which is not standard terminology in machine learning literature.
**Why it needs review:** Consider using "approximately linearly separable" or "nearly linearly separable" for clarity and consistency with standard terminology.

---
