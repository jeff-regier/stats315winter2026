---
## Critique: DATASCI 503, Homework 10: Neural Networks and Deep Learning

### Issues Requiring Review

#### 1. Missing Problem 1(c) - Skipped Subproblem
**Location:** After Problem 1(b), before Problem 1(d)
**Description:** The assignment jumps from part (b) directly to part (d), skipping part (c) from ISLP 10.1.
**Why it needs review:** Instructor must decide whether to add the missing part (c), relabel (d) as (c), or add a note explaining the omission to avoid student confusion.

---

#### 2. Missing Problem 3(a) - Skipped Subproblem
**Location:** Problem 3 header (starts with part b)
**Description:** Problem 3 starts with part (b), skipping part (a) from ISLP 10.4.
**Why it needs review:** Similar to Problem 1, instructor must decide whether to include part (a), relabel parts, or note the intentional omission.

---

#### 3. No Starter Code for Gradient Descent Problems
**Location:** Problems 4(c) and 4(d)
**Description:** Students must implement gradient descent from scratch without a code skeleton or scaffolding.
**Why it needs review:** Pedagogical decision - some instructors prefer providing a skeleton with TODO comments for students unfamiliar with PyTorch autograd, while others want students to figure out the structure themselves.

---

#### 4. Redundant Code Between 4(c) and 4(d)
**Location:** Solution cells for 4(c) and 4(d)
**Description:** The solutions for 4(c) and 4(d) are nearly identical, differing only in the initial beta value (2.3 vs 1.4).
**Why it needs review:** Pedagogical decision about whether to restructure so students write a reusable `run_gradient_descent(beta_init, ...)` function in 4(c) and simply call it with different parameters in 4(d), teaching code reuse principles.

---
