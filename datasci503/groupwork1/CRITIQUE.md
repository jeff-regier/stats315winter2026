---
## Critique: DATASCI 503, Group Work 1: Introduction to Python

### Issues Requiring Review

#### 1. Missing Column Name Clarification (Problem 7)
**Location:** Cell 84
**Description:** The problem references "Sepal length" and "Petal width" but the actual column names are "sepal length (cm)" and "petal width (cm)". Students may waste time figuring out the exact column names.
**Why it needs review:** This is a pedagogical choice - some instructors may prefer students discover the column names themselves as part of the learning process, while others may want to reduce friction by providing exact column names.

#### 2. Problem 8 Ambiguous Requirements
**Location:** Cells 87-89
**Description:** Problem 8 asks students to "write boolean expressions to verify" but the solution uses a list of expressions stored in `verification_results`. It is unclear whether students should just write expressions that evaluate to True, or store them in a specific variable.
**Why it needs review:** Clarifying the expected format is a pedagogical decision about how explicit instructions should be.

#### 3. Problem 6 Free-Response Lacks Guidance
**Location:** Cells 82-83
**Description:** Problem 6 asks what students notice about the summary table but does not specify what aspects they should comment on (e.g., which columns are included/excluded, why certain columns might be missing).
**Why it needs review:** Deciding how much guidance to provide for open-ended questions is a pedagogical choice about student autonomy.

#### 4. Problem 15 RGB Test May Have Incorrect Assertion
**Location:** Cell 116 (hidden tests)
**Description:** The hidden test asserts `np.min(diff_image) == 0` (some pixels unchanged after blurring). However, for most images, a box filter changes all pixel values. This assertion may incorrectly fail for some input images.
**Why it needs review:** Requires verification that the Caltech101 image actually has unchanged pixels after blurring, or the assertion should be removed/modified.

#### 5. No Hint About Integer Division for Problem 14
**Location:** Cell 106
**Description:** The problem states to compute "the floor of the average" but does not hint that Python's `//` operator performs floor division. Students unfamiliar with this operator may struggle.
**Why it needs review:** Deciding whether to add a hint about `//` is a pedagogical choice about scaffolding level.

#### 6. Inconsistent Type Hints Across Functions
**Location:** Various cells
**Description:** Some functions include type hints (e.g., `is_power_of_2(number: int) -> bool`) while others do not (e.g., `get_gross_pay(hours_worked, rate_per_hour)`).
**Why it needs review:** Consistency in type hints is a style decision - either add them to all functions or remove them entirely.

#### 7. Weak Tests for Problem 4 (Student Testing)
**Location:** Cells 76-77
**Description:** Problem 4 asks students to write their own tests using a `student_tests_passed` variable, but this variable is never validated. The test cell re-tests `is_power_of_2` rather than verifying students wrote meaningful tests.
**Why it needs review:** Deciding how to assess student-written tests requires pedagogical judgment about the learning objectives.

---
