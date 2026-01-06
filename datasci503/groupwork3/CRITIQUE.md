---
## Critique: DATASCI 503, Group Work 3: ROC Curves and Logistic Regression

### Issues Requiring Review

#### 1. Division by Zero Edge Case Not Warned in Problem 10
**Location:** Cell 52-53 (Problem 10: Implement ROC from Scratch)
**Description:** The solution handles division by zero for FPR and TPR calculations, but students are not warned about this edge case in the problem description. If students do not handle the case where (FP + TN) = 0 or (TP + FN) = 0, their implementation may fail at extreme thresholds.
**Why it needs review:** Deciding whether to add an explicit hint about edge cases is a pedagogical choice. Adding the hint makes the problem easier but may reduce the learning opportunity for students to discover and handle edge cases themselves.

#### 2. Problem 3 Response Variable Name Inconsistency
**Location:** Cell 30-32 (Problem 3: Select Predictor Variables)
**Description:** The problem mentions "response variable (`LBDHDD` for HDL)" but the solution renames it to `HDL`. This creates confusion in later problems where the code must check for both names using `"HDL" if "HDL" in my_df.columns else "LBDHDD"`.
**Why it needs review:** This is a design decision about whether to require a specific naming convention (always rename to `HDL`), or allow flexibility and have subsequent code handle both cases. The current approach works but is fragile.

#### 3. Problem 5 Threshold Ambiguity (>= vs >)
**Location:** Cell 37-38 (Problem 5: Create Binary HDL Indicator)
**Description:** The problem states HDL of "60 mg/dL or higher" is protective, then asks for a binary indicator that is True when HDL is "**greater than** 60 mg/dL". This is inconsistent - the medical context suggests `>= 60` while the implementation requires `> 60`.
**Why it needs review:** This requires a content decision about the correct medical interpretation. Using `>= 60` would match the quoted medical guidance, but the current tests expect `> 60`.

#### 4. No Warning About NHANES Data File Dependencies
**Location:** Cell 23-24 (Problem 1)
**Description:** The assignment assumes NHANES data files exist at `../datasets/NHANES/` but provides no fallback or error message if files are missing.
**Why it needs review:** Adding file existence checks is a design choice that affects the student experience. It may be intentionally omitted to keep the notebook focused on the learning objectives.

---
