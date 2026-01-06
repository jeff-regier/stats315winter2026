---
## Critique: Group Work 4 - PyTorch Training Pipeline and FashionMNIST

### Issues Requiring Review

#### 1. Test Cell Reveals Model Architecture in Problem 2c
**Location:** Cell 34 (hidden tests)
**Description:** The hidden test assertion `len(list(classification_model.parameters())) == 6` reveals that the model should have exactly 6 parameter tensors, which gives away the architecture structure (3 linear layers with weights and biases).
**Why it needs review:** This is a pedagogical decision about what information should be hidden vs. revealed. You may want to either move this to visible tests with an educational message, remove it entirely, or keep it as a grading sanity check.

#### 2. Learning Objectives Mismatch
**Location:** Cell 0 (title cell)
**Description:** The stated learning objectives mention "Tensors in PyTorch" and "Automatic differentiation (autograd) in PyTorch" but the assignment doesn't explicitly cover tensors (beyond basic usage) or demonstrate autograd concepts directly. Students don't implement any manual gradient computation or tensor operations.
**Why it needs review:** This is a content decision about whether to update the learning objectives to match the actual content (DataLoaders, Sequential models, training loops), or add introductory content covering tensors and autograd explicitly.

#### 3. Problem 2e Complexity
**Location:** Cell 38
**Description:** Problem 2e requires students to implement a complete training loop with multiple components: optimizer initialization, epoch loop, batch loop, forward pass, backward pass, gradient zeroing, test evaluation, and accuracy computation. This is substantial for students learning PyTorch for the first time.
**Why it needs review:** This is a pedagogical choice about scaffolding. Consider whether to break this into multiple sub-steps or provide more scaffolding code (e.g., provide the training loop skeleton and have students fill in specific parts).

#### 4. Cell 17 Reference to "Above"
**Location:** Cell 17
**Description:** States "This is similar to the optimization routine we saw above for simple linear regression" but there is no linear regression optimization example earlier in the notebook - only the synthetic data regression problem with a deep network.
**Why it needs review:** The reference may be intentionally referring to prior course materials or a different assignment. Verify whether this should say "synthetic regression problem" instead of "simple linear regression."

---
