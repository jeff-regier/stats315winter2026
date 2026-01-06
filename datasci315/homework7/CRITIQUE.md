---
## Critique: Homework 7 - Regularization for Image Classification

### Issues Requiring Review

#### 1. Optimizer State Not Reset When Re-training
**Location:** Problem 2, cells 20-25
**Description:** The `reset_model_parameters()` function resets model weights, but when students iterate on hyperparameters and re-run training, the optimizer object retains stale momentum/state from the previous run. The optimizer is created once with `model.parameters()`, and if students change `lr` or `weight_decay` and re-run only the training cell, the optimizer still uses old hyperparameters.
**Why it needs review:** This is a design decision about how to structure the training workflow. Options include: (1) recreate the optimizer inside the `train()` function, (2) add a helper function to reset optimizer state, or (3) add clear instructions that students must re-run the optimizer cell when changing hyperparameters. Each approach has different pedagogical implications.

---

#### 2. Data Files May Not Exist - No Graceful Error Handling
**Location:** Cell 6
**Description:** The code assumes `data/dataset_train_0.5_norm.pt` and `data/dataset_test_0.5_norm.pt` exist. If students haven't downloaded the files or placed them incorrectly, they get a cryptic `FileNotFoundError`.
**Why it needs review:** Deciding whether to add error handling with helpful messages is a content decision. The Canvas download links may also break over time. Consider whether to add a try-except block or file existence check.

---

#### 3. Problem 1 Lacks Guidance on Architecture Design
**Location:** Cells 15-16
**Description:** Students are told to "fill out the below with a model architecture that you think will work well" with no guidance on layer sizes, depth, or dropout placement. The only hint is a link to dropout documentation.
**Why it needs review:** This is a pedagogical choice about how much scaffolding to provide. The assignment is about regularization, not architecture search. Consider whether to provide rough guidance (e.g., "consider 2-4 hidden layers with 128-512 units") or a scaffold with placeholders.

---

#### 4. Problem 2 Training Function Lacks Specification
**Location:** Cells 21-22
**Description:** The function signature and expected behavior are not specified. Students don't know: (1) what loss function to use, (2) whether to return losses per epoch or cumulative, (3) whether to print progress, (4) expected return type.
**Why it needs review:** Deciding how much to specify vs. leaving open-ended is a pedagogical choice. Consider adding a docstring template or explicit requirements like "Use CrossEntropyLoss. Return lists of per-epoch average losses."

---

#### 5. Test for train() Function is Weak
**Location:** Cell 23
**Description:** The test only checks that `train` is callable and has at least 4 parameters. It doesn't verify the function actually trains or returns the correct format.
**Why it needs review:** Strengthening this test would require running training for at least 1 epoch, which has performance implications for autograding. Decide if a more robust test is worth the added execution time.

---

#### 6. No Explanation of L2 Regularization / weight_decay
**Location:** Cells 21, 24-25
**Description:** The assignment mentions `weight_decay` "uses L2 regularization to penalize large weights" but doesn't explain what L2 regularization is or why it helps.
**Why it needs review:** This is a homework on regularization, so conceptual understanding may be important. Consider adding a brief explanation, a link to documentation, or a question asking students to explain why weight decay helps.

---

#### 7. Batch Size Cell Has Mixed Student/Solution Content
**Location:** Cell 28
**Description:** `batch_size = 256 # SOLUTION` but the rest of the cell (DataLoader setup) is not marked as solution. Students will see the DataLoader code but must fill in batch_size.
**Why it needs review:** Decide whether this mixed structure is intentional or if the entire cell should be marked as solution, or the batch_size definition separated from the DataLoader setup.

---
