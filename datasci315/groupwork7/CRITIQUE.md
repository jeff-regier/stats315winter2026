---
## Critique: Group Work 7 - High-Dimensional Spaces, Bias-Variance Trade-Off, Ensemble Methods, and Data Augmentation

### Issues Requiring Review

#### 1. Missing Starter Code / Skeleton Functions
**Location:** Problems 1a (cell 5), 1b (cell 9), 2a (cell 21), 4a (cell 54), 4c (cell 65)
**Description:** The solution cells contain complete implementations without any starter code structure for students. The student version will be completely empty.
**Why it needs review:** This is a pedagogical decision. Some instructors prefer students write from scratch, while others prefer skeleton functions with docstrings, type hints, and `raise NotImplementedError()` placeholders.

#### 2. Missing Documentation Links
**Location:** Throughout, but especially Parts B and C
**Description:** No links to PyTorch documentation for `torch.linalg.norm`, `nn.CrossEntropyLoss`, `StepLR`, `DataLoader`, etc.
**Why it needs review:** Deciding which documentation links to include is a pedagogical choice about how much scaffolding to provide students.

#### 3. Textbook Figure References Without Context
**Location:** Problems 2b, 2c, 2d reference "Figure 8.6", "Figure 8.7", "Figure 8.9"
**Description:** Textbook figures are referenced without providing the textbook name or showing what the figures look like.
**Why it needs review:** This may be intentional if students have access to the textbook ("Understanding Deep Learning" by Simon Prince), but could confuse students without context.

#### 4. Problem 4a Missing Clear Problem Statement
**Location:** Cell 53-54
**Description:** Problem 4a says "Training Function for MNIST-1D" with a hint about StepLR, but doesn't clearly state what the student needs to implement. The entire training function is in the solution.
**Why it needs review:** Needs instructor decision on whether this is meant to be a "read and understand" problem or if students should implement parts of it.

#### 5. Problem 4e Lacks Clear Requirements
**Location:** Cell 72-73
**Description:** "Achieve 70% Accuracy" doesn't specify constraints. Can students use any architecture? Any augmentation? Any training parameters?
**Why it needs review:** Needs clarification on what constraints (if any) students should follow when tuning for 70% accuracy.

#### 6. Problem 2a Uses Global Variable x_model
**Location:** Cell 21
**Description:** The function `get_model_mean_variance` references `x_model` which is defined in cell 18 (after the helper code section), but Problem 2a appears after that. Students may not realize this dependency.
**Why it needs review:** Decide whether to pass `x_model` as a parameter or add a note explaining the global variable dependency.

#### 7. Problem 4e Redefines augment Function with Different Scaling
**Location:** Cell 73
**Description:** Problem 4e redefines the `augment` function with element-wise scaling [0.95, 1.05] instead of the scalar scaling [0.8, 1.2] from Problem 4c. This overwrites the previous definition.
**Why it needs review:** This may be intentional to show students different augmentation approaches, but could be confusing. Consider whether this should be a separate function or if the difference should be explained.

#### 8. weights_init Function Appears Without Context
**Location:** Cell 51
**Description:** The `weights_init` function appears between visualization code and the MNIST-1D section without any explanation of what it does or why He initialization is needed.
**Why it needs review:** Consider adding a markdown cell explaining He initialization and why it's important for deep networks, or if students are expected to already know this.

---
