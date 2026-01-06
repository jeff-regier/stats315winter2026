---
## Critique: DATASCI 315, Group Work 3: Logistic Regression and Maximum Likelihood

### Issues Requiring Review

#### 1. Inconsistent Intercept Handling Between Problems 4 and 5
**Location:** Problem 4 (cell-24) and Problem 5 (cell-28/29)
**Description:** Problem 4 states "Assume the intercept vector is already included in X" but Problem 5's solution adds the intercept column inside the function. The test for Problem 5 passes `initial_w` with shape `(p+1, 1)` expecting the function to handle intercept internally.
**Why it needs review:** This is a design decision about the assignment structure. Either (a) Problem 4 should also have students add the intercept, or (b) Problem 5 should expect the intercept pre-added. The current inconsistency may confuse students about the expected convention.

#### 2. Sigmoid Function Numerical Stability
**Location:** Problem 4 (cell-26)
**Description:** The sigmoid implementation `1 / (1 + torch.exp(-z))` can produce NaN or Inf values for large positive or negative z values due to exp overflow.
**Why it needs review:** This is a pedagogical choice. Options include: (a) keeping the simple formula since data is standardized, (b) adding a note about numerical stability, or (c) teaching the numerically stable form. The current approach works for the standardized data used in this assignment but students should understand the limitation.

#### 3. Text Reference to "54% Confidence" May Not Match Output
**Location:** Cell-21 (markdown)
**Description:** The text states "the model only has 54% confidence on the label it predicted" but this specific value may not match what students see when they run the notebook, depending on sklearn version or other factors.
**Why it needs review:** The specific percentage mentioned may need updating if it doesn't match the actual output, or the text could be generalized to not reference a specific value.

---
