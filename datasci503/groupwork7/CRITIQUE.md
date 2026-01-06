---
## Critique: DATASCI 503, Group Work 7: Trees and Tree Ensembles

### Issues Requiring Review

#### 1. Missing Data Files for Problem 2
**Location:** Problem 2 (cell-56, cell-57)
**Description:** The problem asks students to load NHANES data files (`BMX_L.xpt`, `DEMO_L.xpt`, `HDL_L.xpt`) from a `data/` directory, but there is no indication that these files are provided or instructions on how to obtain them.
**Why it needs review:** Students cannot complete Problems 2-10 without access to these data files. The assignment provides a download mechanism for the spambase dataset but not for the NHANES dataset. A decision must be made whether to (a) add code to download the NHANES .xpt files programmatically, (b) provide explicit instructions with download URLs, or (c) ensure the data files are included in the assignment distribution.

#### 2. Problem 6 Visible Tests Depend on Specific Row Indices
**Location:** Problem 6 test cell (cell-70)
**Description:** The visible tests check specific row indices (`my_df.iloc[6]`, `my_df.iloc[155]`, `my_df.iloc[20]`) for expected Level values. After dropping NaN values, the row indices may shift unpredictably depending on which rows had missing values.
**Why it needs review:** Students with correct implementations may fail these tests if the DataFrame indices don't align after `dropna()`. Consider either requiring index reset in Problem 2, or using more robust tests that don't depend on specific row positions.

#### 3. Problem 10 Accuracy Threshold May Be Arbitrary
**Location:** Problem 10 (cell-82, cell-84)
**Description:** The 57% accuracy threshold is provided without context about baseline performance or class distribution.
**Why it needs review:** Students may not understand what constitutes good performance for this task. Consider adding context about baseline accuracy (e.g., majority class predictor) to help students interpret their results.

#### 4. Problem 9b Expected Answer Depends on Random Results
**Location:** Problem 9b (cell-81)
**Description:** The solution notes "The exact ranking may vary depending on the random state and data split," but the problem prompt doesn't acknowledge this variability to students.
**Why it needs review:** Students may be confused if their ranking differs from the expected answer. Consider either explaining variability in the prompt or restructuring the question to focus on methodology rather than a specific ranking.

#### 5. Problem 6 HDL Threshold Citation
**Location:** Problem 6 (cell-68)
**Description:** The Cleveland Clinic thresholds are cited, but medical thresholds can vary by source.
**Why it needs review:** Consider noting that thresholds can vary by source, or verifying that the Cleveland Clinic values are current and widely accepted.

---
