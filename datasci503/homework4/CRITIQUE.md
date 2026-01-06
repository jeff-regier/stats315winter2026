---
## Critique: DATASCI 503, Homework 4: Classification

### Issues Requiring Review

#### 1. Missing Section Header Before Problem 5
**Location:** Cell 11 (markdown cell introducing "LDA Decision Boundary")
**Description:** Cell 11 introduces a new section "LDA Decision Boundary" with setup information but is not formatted as a proper section header with `##` formatting. This breaks the structural flow.
**Why it needs review:** Formatting section headers is a pedagogical and structural choice. The current text provides context but may cause confusion about the relationship between the setup and following problems.

---

#### 2. Inconsistent Section Header Formatting
**Location:** Throughout the assignment (Problems 1-4, 5-9, 10-12, 13-21)
**Description:** The assignment has 21 problems across different sections but lacks consistent `##` section headers for all topic transitions. Currently only "LDA Decision Boundary", "Stock Market Prediction", and "Auto MPG Classification" have section markers.
**Why it needs review:** Adding section headers like "Theoretical Foundations" (Problems 1-4) would improve navigation but may not align with the intended document structure.

---

#### 3. Problem 14 Has Vague Requirements
**Location:** Cell 41 (Problem 14)
**Description:** The problem asks students to identify "four quantitative features" but doesn't clarify whether `origin` should be considered quantitative, or what constitutes a sufficient defense of their selection.
**Why it needs review:** Clarifying requirements (e.g., "Choose four quantitative features from: cylinders, displacement, horsepower, weight, acceleration, and year") is a content decision that may affect grading expectations.

---

#### 4. No Test Cell for Problem 10 (EDA)
**Location:** After cells 28-29
**Description:** Problem 10 asks for exploratory data analysis but has no test assertions to verify completion.
**Why it needs review:** This appears to be a free-response problem. Decide whether to add a basic test (e.g., validate a figure was created) or explicitly mark it as free-response.

---

#### 5. No Test Cell for Problem 14 (EDA)
**Location:** After cells 42-43
**Description:** Problem 14 requires students to select features and create plots but has no test cell to verify the exploration was completed.
**Why it needs review:** This appears to be a free-response problem. Decide whether to add structure (e.g., storing selected features in a testable list) or keep it as free-response.

---

#### 6. Data File Paths Not Verified
**Location:** Cells 26 and 37
**Description:** The assignment loads data from `./data/Smarket.csv` and `./data/auto_nonan.csv` but provides no guidance if these files don't exist.
**Why it needs review:** Adding a markdown cell explaining data sources or adding try/except blocks with helpful error messages is a content decision that affects student experience.

---

#### 7. Feature Selection Flow Ambiguity
**Location:** Problems 14-15
**Description:** Problem 14 asks students to qualitatively select "four quantitative features," but Problem 15 uses a specific set of features (`cylinders`, `displacement`, `horsepower`, `weight`) in the solution. Students who chose different features in Problem 14 may be confused.
**Why it needs review:** Either make Problem 14 store selected features in a variable that Problem 15 uses, or explicitly state which four features to use in Problem 15. This is a pedagogical decision about whether to allow flexibility in feature selection.

---
