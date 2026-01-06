---
## Critique: DATASCI 503, Homework 8: Support Vector Machines

### Issues Requiring Review

#### 1. Missing Data File and No Instructions for Obtaining It
**Location:** Problem 4, cell-10
**Description:** The code references `data/crabs.csv` but there are no instructions for students on where to obtain this data file or how to load it.
**Why it needs review:** Students cannot complete Problem 4 without the data file. The decision of whether to include the file in the repository, provide a download URL, or add loading code from a URL is a content/data handling decision that requires human judgment.

---

#### 2. Problem 4 Lacks Clear Deliverables and Analysis Questions
**Location:** Problem 4 (a), (b), (c)
**Description:** Each part asks students to "plot" and test various hyperparameters but never asks them to interpret results, compare kernel performance, or draw conclusions about which model is best.
**Why it needs review:** Adding interpretation questions (e.g., comparing kernels, explaining results, evaluating on test set) is a pedagogical choice that affects the assignment's learning objectives and scope.

---

#### 3. No Explanation of the C Hyperparameter
**Location:** Problem 4 introduction
**Description:** The assignment introduction mentions slack variables but Problem 4 jumps directly to tuning C without explaining what C controls or how it relates to soft-margin SVM concepts from Problems 2-3.
**Why it needs review:** Whether to add conceptual scaffolding linking Problems 2-3 to Problem 4's hyperparameter tuning is a pedagogical design decision.

---

#### 4. No Guidance on C Value Range Selection
**Location:** Problem 4
**Description:** Students are told to test "a range of values of the C hyperparameter" but given no guidance on what range is reasonable or how to select it.
**Why it needs review:** Deciding whether to provide explicit C ranges, recommend logarithmic spacing, or leave it open-ended affects the assignment difficulty and learning objectives.

---

#### 5. Gamma Values Should Consider Logarithmic Scale
**Location:** Problem 4(c)
**Description:** The problem asks for "at least three values of gamma" without recommending logarithmic spacing, which is standard practice for kernel hyperparameters.
**Why it needs review:** Recommending log-scale for gamma is a pedagogical choice that could either be taught explicitly or left for students to discover.

---

#### 6. ISLP Textbook References May Be Inaccessible
**Location:** Problems 1 and 2
**Description:** Problems 1 and 2 reference "ISLP 9.2", "ISLP 9.3", and "equation (9.1) in ISLP" which require access to the ISLP textbook.
**Why it needs review:** Whether these references are appropriate depends on whether all students have textbook access. This is a content/copyright consideration.

---

#### 7. No Random Seed Guidance in Problem Instructions
**Location:** Problem 4
**Description:** While the solution uses `random_state=42` for KFold, students are not instructed to use a specific seed, which may cause different results.
**Why it needs review:** Deciding whether reproducibility should be required or left to students is a pedagogical choice affecting grading consistency.

---
