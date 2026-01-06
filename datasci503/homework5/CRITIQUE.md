---
## Critique: DATASCI 503, Homework 5: Resampling Methods

### Issues Requiring Review

#### 1. Missing Data File Documentation
**Location:** Cells 35, 69
**Description:** The assignment references `./data/boston.csv` and `./data/weekly.csv` without specifying where students can obtain these files or confirming they will be provided.
**Why it needs review:** Instructors need to decide whether to add a setup cell explaining data file locations, provide download instructions, or confirm that files are already distributed with the assignment.

---

#### 2. Boston Dataset Context and Ethical Considerations
**Location:** Cell 34 (Problem 5 introduction)
**Description:** Problem 5 references "the Boston housing data set" without explaining what the dataset contains, what `medv` represents, or noting that this dataset has been deprecated in sklearn due to ethical concerns about its creation.
**Why it needs review:** Instructors should decide whether to add context about the dataset variables and whether to acknowledge ethical issues or suggest an alternative dataset.

---

#### 3. Inconsistent Random Seed Usage
**Location:** Cells 43-44, 57, 65 vs. Cell 21
**Description:** The bootstrap function uses `seed=2024` in later problems, but Problem 3(a) uses `rng = np.random.default_rng(1)`. This inconsistency could confuse students about reproducibility practices.
**Why it needs review:** Instructors should decide whether to standardize seeding conventions throughout the assignment or add an explanation for why different seeds are used.

---
