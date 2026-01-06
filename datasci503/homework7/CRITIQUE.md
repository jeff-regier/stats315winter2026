---
## Critique: DATASCI 503, Homework 7: Ensemble Methods and Decision Trees

### Issues Requiring Review

#### 1. Problem 3 Embedded Images May Not Be Accessible
**Location:** Cell 5 (Problem 3: Classification Tree Sketches)
**Description:** The problem references `attachment:Picture_A.jpg` and `attachment:Picture_B.jpg` which are embedded attachments. These images may not render properly in all environments (GitHub, exports, or if attachments are stripped).
**Why it needs review:** Students may not be able to see the images, making the problem unsolvable. Consider either (a) placing images in a `data/` or `images/` folder with relative paths, (b) providing a textual description, or (c) removing this problem entirely.

---

#### 2. Problem 3 Lacks Specific Questions and Has Inadequate Solution
**Location:** Cell 5-6 (Problem 3)
**Description:** The problem asks students to analyze "sketches" but provides no specific questions or tasks. The solution merely states "The sketches above illustrate the partitioning of feature space by decision trees" without substantive analysis.
**Why it needs review:** Without specific questions, there is no way to evaluate student responses. Consider adding concrete questions (e.g., "Describe the decision boundaries", "How many terminal nodes are shown?") or replacing with a code-based visualization task.

---

#### 3. Variable Importance Comparison Answer is Imprecise
**Location:** Cell 20 (Problem 6 solution)
**Description:** The solution says "FL... may be further down the list" which is vague. Solutions should provide concrete expected observations.
**Why it needs review:** Decide whether the solution should be more specific about expected results, or whether the vagueness is intentional to account for variation across runs.

---

#### 4. Hardcoded Optimal M Value
**Location:** Cell 25
**Description:** `optimal_m = 40` is hardcoded in the solution rather than being derived programmatically from the error curves.
**Why it needs review:** Decide if students should be required to programmatically determine this value (e.g., by finding the M that minimizes test error), or if manual selection based on visual inspection of the plot is acceptable.

---
