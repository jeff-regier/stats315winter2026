---
## Critique: DATASCI 503, Homework 1: Introduction to Statistical Learning

### Issues Requiring Review

#### 1. Problem 5e Doesn't Fit the "Data Analysis with Pandas" Section
**Location:** Problem 5e (cell-25 to cell-27)
**Description:** The "For Loops" problem asks students to generate "Hello world" strings, which has nothing to do with pandas or data analysis. It appears under the "Data Analysis with Pandas" section.
**Why it needs review:** This is a pedagogical decision about course structure. Options include: moving this problem to a separate "Python Fundamentals" section, replacing it with a pandas-related for loop exercise (e.g., iterating over DataFrame rows), or keeping it as a transitional exercise to reinforce Python basics.

#### 2. Problem 4 Solutions Lack Explanations
**Location:** Problem 4 (cell-10)
**Description:** The solutions for Problem 4 (Asymptotic Properties) provide True/False answers with minimal explanation, unlike Problem 3 which includes brief justifications.
**Why it needs review:** Pedagogical choice about solution detail. Adding explanations (e.g., why KNN variance doesn't go to zero, why linear regression bias doesn't go to zero) would improve consistency and educational value, but may be intentionally brief.

#### 3. Inconsistent Problem Numbering Scheme
**Location:** Problems 1-4 vs Problems 5a-5f
**Description:** Problems 1-4 use sub-parts (a), (b), (c) within a single problem, but the pandas section uses 5a, 5b, 5c, etc. as separate standalone problems. This creates inconsistency about what constitutes a "problem."
**Why it needs review:** Style decision. Options: make 5a-5f sub-parts of Problem 5 (consistent with Problems 1-4), or renumber them as Problems 5-10.

#### 4. Problem 5f Cannot Be Autograded
**Location:** Problem 5f (cell-28 to cell-29)
**Description:** This problem asks students to create a markdown cell, but there's no way to automatically test markdown formatting. The solution is provided but has no test assertions.
**Why it needs review:** Grading approach decision. Options include: making it explicitly ungraded with a note, removing the problem, or converting it to a code problem that generates markdown strings that can be tested.

#### 5. No Data Dictionary or Column Descriptions
**Location:** After cell loading college_train.csv (cell-11 and cell-12)
**Description:** Students are asked to work with columns like "Books", "Terminal", and "Private" without any explanation of what these variables represent.
**Why it needs review:** Content decision about how much context to provide. Adding a data dictionary would improve educational value but may be intentionally omitted to encourage exploration.

#### 6. Problem 2 Answer Format Inconsistency
**Location:** Problem 2 solutions (cell-6)
**Description:** The question asks for classification vs regression first, then inference vs prediction. The solutions use "Type of problem - Inference (more specifically regression)" which conflates the order.
**Why it needs review:** May be intentionally structured this way for pedagogical reasons, or could be reformatted for clarity.

#### 7. No Submission Instructions
**Location:** End of notebook
**Description:** The assignment doesn't mention how students should submit or what format is expected.
**Why it needs review:** May be provided separately (e.g., on course website) or may need to be added to the notebook.

---
