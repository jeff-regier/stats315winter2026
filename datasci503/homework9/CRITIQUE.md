---
## Critique: DATASCI 503, Homework 9: Clustering and Principal Component Analysis

### Issues Requiring Review

#### 1. Potentially Incorrect Usage of scipy.cluster.hierarchy.linkage with Full Dissimilarity Matrix
**Location:** Cell 3 (Problem 1a hint) and Cell 4 (solution)

**Description:** The hint says to pass the full dissimilarity matrix directly to `linkage()`. However, `scipy.cluster.hierarchy.linkage()` expects either a condensed distance matrix (1D array from `squareform`) or a 2D observation matrix where it computes distances. Passing a full 4x4 symmetric matrix treats each row as a 4-dimensional observation and computes Euclidean distances between rows, which is NOT the same as using the given pairwise dissimilarities.

**Why it needs review:** This fundamentally affects whether Question 1 produces correct results. The instructor needs to verify whether the current approach produces the intended clustering or if it should be converted using `scipy.spatial.distance.squareform(dissimilarity_matrix)` before passing to `linkage()`. This affects the entire first question and all its parts.

---

#### 2. Hidden Test in Problem 1e May Have False Assumptions
**Location:** Cell 17 (test cell for Problem 1e)

**Description:** The hidden test asserts `linkage_reordered[0, 2] == linkage_complete[0, 2]` (first merge distance should match). While this seems correct for this specific reordering that preserves the 1-2 and 3-4 pairs, the test comment says "Merge distances should match" which could be misleading if students use a different reordering.

**Why it needs review:** The instructor should verify whether the test is specific enough to the required [2,1,4,3] reordering or if it should be more robust to different valid reorderings.

---

#### 3. Test Asserts Exactly 5 Clusters at t=75
**Location:** Cell 32 (Problem 3b test)

**Description:** The test asserts `num_clusters == 5` when cutting at `t=75`. This hard-coded assertion ties the expected answer to the specific dataset and threshold.

**Why it needs review:** The instructor should confirm this is the intended pedagogical approach (specifying both threshold and expected result) versus asking students to find an appropriate threshold for 5 clusters, which would be a different learning objective.

---

#### 4. 1-Indexed K-Means Labels Non-Standard
**Location:** Cell 36-37 (Problem 3c)

**Description:** The solution adds 1 to K-means labels to make them 1-indexed "for consistency with hierarchical clustering." This deviates from scikit-learn conventions (0-indexed) and adds complexity.

**Why it needs review:** The instructor should decide whether to keep 1-indexing for visual consistency with hierarchical labels or switch to 0-indexing for Python conventions. The hidden test enforces 1-indexing.

---

#### 5. Problem 3d Missing Interpretation Question
**Location:** Cell 39 (Problem 3d)

**Description:** The problem asks students to compare silhouette scores with and without scaling but doesn't require them to interpret or discuss why the results differ.

**Why it needs review:** The instructor may want to add a free-response component asking students to explain the effect of scaling on clustering results, which would strengthen the pedagogical value.

---

#### 6. PCA on Unscaled Data Without Explanation
**Location:** Cell 43-45 (Problem 3e)

**Description:** PCA is applied to unscaled data, and the hidden test checks that PC1 explains >90% variance. This is expected since Assault has much larger values than other features, but no pedagogical note explains this is demonstrating a common pitfall.

**Why it needs review:** The instructor should consider whether to add a follow-up problem with scaled PCA for comparison, or add a discussion question about why PC1 dominates when data is unscaled.

---

#### 7. Warnings Suppression
**Location:** Cell 1

**Description:** The notebook includes `warnings.filterwarnings("ignore")` which hides all warnings including potentially useful deprecation warnings.

**Why it needs review:** The instructor should decide if this is intentional to reduce output clutter or if students should see warnings as part of their learning experience.

---
