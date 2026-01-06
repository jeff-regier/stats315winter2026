---
## Critique: DATASCI 503, Homework 2: K-Nearest Neighbors and Bias-Variance Tradeoff

### Issues Requiring Review

#### 1. Clarification of Squared vs Regular Euclidean Distance
**Location:** Cell 2 (K-NN introduction) and Problem 1a
**Description:** The assignment uses squared Euclidean distance without explaining that it preserves the same ordering as regular Euclidean distance for finding nearest neighbors.
**Why it needs review:** Students computing regular Euclidean distance (with square roots) will get different numeric answers but correct classifications. The instructor should decide whether to: (1) add a note explaining the equivalence for ordering purposes, or (2) explicitly require squared distance in the problem statement with this explanation.

#### 2. Problem 3c Scaffolding for Broadcasting
**Location:** Cell 21 (Problem 3c statement)
**Description:** Students must generate data from a conditional uniform distribution using `np.random.uniform(low, high, size)` with array bounds, which requires understanding NumPy broadcasting.
**Why it needs review:** The instructor should decide whether to add a hint about `np.random.uniform` accepting array bounds, or whether this is an intentional learning challenge for the course level.

#### 3. Problem 1d Terminology Precision
**Location:** Cell 9 (Problem 1d statement)
**Description:** The phrase "In a typical data-generating process" is somewhat vague.
**Why it needs review:** The instructor may want to specify more precisely what conditions make K=3 more consistent than K=1 (e.g., "when outliers and noise are present" or "when the Bayes decision boundary is smooth").

#### 4. Problem 3b Exact vs Approximate Value
**Location:** Cell 20 (Problem 3b solution)
**Description:** The solution shows the variance as approximately 0.00333 but the exact value is 1/300.
**Why it needs review:** The instructor should decide whether showing the exact fraction (1/300) would be more pedagogically valuable alongside the decimal approximation.

---
