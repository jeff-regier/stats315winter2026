---
## Critique: Homework 6 - Training Models with PyTorch

### Issues Requiring Review

#### 1. Global Variable Dependency in Model Function (Problem 2c)
**Location:** Cell cell-23 (model function definition)
**Description:** The `model` function references global variables `W1`, `b1`, `W2`, `b2` directly rather than accepting them as parameters. This creates tight coupling between the model and the specific weight tensors defined in Problem 2b.
**Why it needs review:** This is a pedagogical design decision. Options include: (1) pass weights as parameters, (2) wrap in a class structure, or (3) explicitly document this design choice. Human judgment needed on whether the current approach is acceptable for this educational context or if refactoring would improve learning outcomes.

---

#### 2. Inconsistent Model Output Shape (Problem 2c)
**Location:** Cell cell-23 and cell-24
**Description:** The problem states the model should return a tensor of shape `(n,)`, but the model returns shape `(n, 1)` because `W2` has shape `(hidden_dim, output_dim)` where `output_dim=1`. The solution uses `.squeeze()` in the MSE function to handle this.
**Why it needs review:** Human judgment needed on whether to: (1) update instructions to say the model returns shape `(n, 1)`, (2) instruct students to squeeze in the model function, or (3) leave as-is with the squeeze in MSE handling it.

---

#### 3. Missing Random Seed in Problem 2b
**Location:** Cell cell-20
**Description:** Problem 2b asks students to initialize weights with random values but does not set a random seed, making debugging harder for students.
**Why it needs review:** Decide whether to add `torch.manual_seed(...)` before the solution cell, or acknowledge that random initialization will vary. This affects reproducibility for students debugging their code.

---

#### 4. Overwriting Variable Names in Problem 3a
**Location:** Cell cell-36
**Description:** The solution overwrites `digit_images` and `digit_labels` from numpy arrays to torch tensors. If a student runs the cell multiple times or out of order, they will get errors.
**Why it needs review:** Decide whether to: (1) use different variable names like `digit_images_tensor`, (2) document that the cell should only be run once, or (3) leave as-is since re-running all cells from the start is standard practice.

---

#### 5. Ambiguous "Average Loss" in Problem 3d
**Location:** Cell cell-46
**Description:** The problem asks students to compute "average loss over the training data" but the solution computes `epoch_training_loss / len(train_dataloader)`, which is average loss per batch, not per sample.
**Why it needs review:** Clarify whether "average loss" means per-sample or per-batch. These values are different unless all batches have the same size (the last batch may be smaller).

---

#### 6. Hidden Test Potentially Gives Away Solution (Problem 1c)
**Location:** Cell cell-11 and cell-12
**Description:** The hidden test reveals that normalized w1 should be approximately -0.8, and the verification cell shows the true weights. This could give away the expected answer structure.
**Why it needs review:** Decide whether to tighten tolerance, remove or relocate the verification cell, or leave as-is since verification cells are educational.

---

#### 7. Minor Clarity Issues
**Location:** Various cells
**Description:** Several minor issues that may benefit from review:
- Problem 1a hint about `y -> 2y-1` transformation could be clearer
- Problem 2d silently drops the last batch if `num_samples` is not divisible by `batch_size`
- Problem 3b has a question ("How many total parameters?") but no explicit instruction to answer it

**Why it needs review:** These are minor pedagogical choices about hint clarity and implicit expectations.

---
