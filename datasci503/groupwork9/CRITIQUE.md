---
## Critique: DATASCI 503, Group Work 9: PCA and Clustering

### Issues Requiring Review

#### 1. Variable Naming Inconsistency in Problem 5
**Location:** Cells 52-54
**Description:** The problem asks students to create `X = ZL + epsilon`, but the solution uses different variable names (`latent_samples`, `projection_matrix`, `data_matrix`). The test cell references these solution-specific variable names, which students would not know to use.
**Why it needs review:** This is a pedagogical decision - either the problem statement should specify exact variable names, or the mathematical notation (`Z`, `L`, `X`) should be used consistently. This affects how students approach the problem and whether tests will pass.

#### 2. Variable Requirements Not Specified in Problem 7
**Location:** Cells 59-61
**Description:** The test cell checks for `pca_model` and `explained_variance_cumsum`, but these variable names are not specified in the problem statement. Students may use different names and fail the tests.
**Why it needs review:** Requires deciding whether to explicitly specify variable names in the problem or adjust tests to be more flexible.

#### 3. Problems 6 and 8a Have Identical Structure
**Location:** Cells 55-56 and 64-66
**Description:** Problems 6 and 8a are essentially the same task (create 2x3 subplot grid with K-means clustering), just on different data (raw vs PCA-transformed). This may feel repetitive to students.
**Why it needs review:** This is a pedagogical choice - the repetition may be intentional to reinforce the skill, or the problems could be combined or differentiated with additional analysis requirements.

#### 4. Variable Shadowing in Review Section
**Location:** Cell 28
**Description:** The plotly dendrogram example uses `X` as a variable name, which shadows the pandas `X` from the crabs dataset section. This could cause confusion if students run cells out of order.
**Why it needs review:** Deciding whether to rename the variable (e.g., `X_dendrogram`) affects the flow of the review section and whether it should remain unchanged for pedagogical clarity.

---
