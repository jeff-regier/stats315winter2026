---
## Critique: DATASCI 503, Group Work 5: Cross Validation

### Issues Requiring Review

#### 1. Missing Data Files or File Path Specification
**Location:** Problem 1 (cell 38)
**Description:** The solution assumes data files exist at `data/BMX_L.xpt`, `data/DEMO_L.xpt`, and `data/HDL_L.xpt`, but the assignment never tells students where to find these files or confirms they exist in that location.
**Why it needs review:** Students cannot complete the assignment if the data files are not present or if they don't know the correct path. A human decision is needed on whether to add download links, data setup instructions, or confirm the file paths are correct for the course infrastructure.

#### 2. Using KFold Instead of StratifiedKFold in Problem 4
**Location:** Problem 4 (cell 47)
**Description:** Problem 3 correctly emphasizes using stratified sampling in train_test_split, but the KFoldCV function in Problem 4 uses regular KFold rather than StratifiedKFold. This is inconsistent with the earlier stratification reasoning.
**Why it needs review:** This is a pedagogical choice. Either StratifiedKFold should be used for consistency, or an explanation should be added about why stratification is less critical for cross-validation folds.

#### 3. Problem 7b Wording About "Merged Train+Val Dataset"
**Location:** Problem 7b (cell 63)
**Description:** The question asks about retraining on "merged train+val dataset" but the assignment never explicitly separated a validation set from training. Cross-validation uses temporary folds, not a held-out validation set.
**Why it needs review:** The wording may confuse students about the methodology. Consider rewording to "Explain why we retrain the model on the full training set (all data except the test set) before final evaluation."

#### 4. Stack Exchange Link Stability
**Location:** Bias-Variance section (cell 35)
**Description:** The link to Stack Exchange (`stats.stackexchange.com`) for bias-variance tradeoff information may not be a stable long-term reference.
**Why it needs review:** A decision is needed on whether to keep this external link or replace it with a reference to textbook or course materials for long-term stability.

#### 5. KFoldCV_L2 and KFoldCV_NN Use .iloc Indexing
**Location:** Problems 6a and 9 (cells 55, 73)
**Description:** The solutions use `X.iloc[train_idx]` and `y.iloc[train_idx]`, which only works for pandas DataFrames/Series. If a student passes numpy arrays, this will fail.
**Why it needs review:** This is a design decision. Either the functions should be documented as requiring DataFrames, or they should be modified to work with both arrays and DataFrames using bracket indexing.

---
