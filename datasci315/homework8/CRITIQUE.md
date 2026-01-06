---
## Critique: Homework 8 - Fashion MNIST with Regularization

### Issues Requiring Review

#### 1. Test Assertions May Fail Non-Deterministically
**Location:** All test cells (Problems 1-7)
**Description:** Due to random weight initialization and random batch ordering from `random_split`, the exact loss values can vary between runs. Assertions checking specific numeric thresholds (e.g., `training_losses_1[-1] > 1.0`) may pass or fail depending on the random state.
**Why it needs review:** Deciding whether to add `torch.manual_seed(42)` for reproducibility, widen tolerance thresholds, or accept occasional test flakiness is a pedagogical and practical choice that affects both grading reliability and student experience.

#### 2. Missing Conceptual Questions After Problems 1-2
**Location:** After Problems 1 and 2
**Description:** The assignment focuses entirely on implementation without requiring students to explain their understanding of underfitting/overfitting. Students could complete Problems 1-2 by copying hints without understanding why different architectures cause these behaviors.
**Why it needs review:** Adding conceptual questions is a pedagogical design decision. It would increase assignment length but ensure deeper understanding. Problem 8 partially addresses this but comes after all implementation is complete.

#### 3. Problems 4-7 Follow Repetitive Pattern
**Location:** Problems 4, 5, 6, 7
**Description:** All four problems follow the same pattern: copy Problem 2's architecture, add one regularization technique, train, and observe. The hints essentially provide the solution each time.
**Why it needs review:** This repetition may be intentional scaffolding for beginners, or it could be an opportunity to encourage more independent exploration. Combining problems or removing hints from later problems would change the learning experience significantly.

---
