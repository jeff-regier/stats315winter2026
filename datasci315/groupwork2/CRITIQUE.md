---
## Critique: Group Work 2 - Shallow Neural Networks

### Issues Requiring Review

#### 1. Inconsistent Training Data Between Parts
**Location:** Cells 6 and 82
**Description:** The assignment defines `x_train` and `y_train` twice with different values. Part 1 uses one dataset (cell 6), and Part 3 redefines them with different y-values (cell 82). For example, y_train[0] is -0.15934537 in Part 1 but -0.25934537 in Part 3.
**Why it needs review:** This may be intentional for pedagogical reasons (different datasets for different parts), but could confuse students who compare outputs. Decision needed on whether to use distinct variable names (e.g., `x_train_1`, `x_train_3`) or add explicit notes clarifying this is intentional.

#### 2. ReLU Function Defined Twice with Different Implementations
**Location:** Cells 4 and 42
**Description:** The `relu` function is defined twice with different implementations:
- Cell 4: `torch.maximum(x, torch.zeros_like(x))`
- Cell 42: `torch.clamp(preactivation, min=0.0)`
**Why it needs review:** This may be intentional to show students equivalent approaches, but could also cause confusion. Decision needed on whether to consolidate implementations or add a note explaining the equivalent approaches.

#### 3. Missing Textbook Citation/Link
**Location:** Cells 15, 52-53, 66, 81
**Description:** Multiple references to "the Textbook" (Understanding Deep Learning) with figure and equation numbers (e.g., "Figure 3.4", "equation 4.15", "figure 4.6", "figures 5.4 and 5.5b") but no link to the textbook or proper citation.
**Why it needs review:** Students need access to these referenced figures and equations. A link to the textbook (if freely available) or proper citation is needed.

#### 4. Problem 2 Visible Tests Reveal Structure
**Location:** Cell 18
**Description:** The visible tests explicitly check `model.layer1.weights.shape == (3, 1)` which tells students exactly what data structure to use, potentially reducing the learning challenge.
**Why it needs review:** Pedagogical decision needed on whether revealing the expected structure helps students learn or removes valuable discovery. Consider moving structural checks to hidden tests if the goal is for students to figure out the structure themselves.

#### 5. No Scaffolding for Problem 4 Cross-Entropy Loss
**Location:** Cells 32-37
**Description:** Problem 4 asks students to build a classifier and uses the provided `binary_cross_entropy` function, but there's no task asking students to understand or compute anything with the loss. Cell 37 just runs the loss function without any assertion or discussion.
**Why it needs review:** Pedagogical decision needed on whether to add a sub-problem asking students to explain what cross-entropy loss measures, add assertions checking the loss is in a reasonable range, or leave as-is since the focus is on network architecture.

#### 6. Problem 3 Expected Loss Value May Cause Cascading Failure
**Location:** Cells 21-22
**Description:** The problem states "it should be approximately 9.385" for the loss, but this depends on the model parameters set in Problem 2. If students make any error in Problem 2, this cascading failure will be confusing.
**Why it needs review:** Decision needed on whether to add a note that the expected value assumes correct completion of Problem 2, or reset the model parameters at the start of Problem 3 to isolate the problems.

---
