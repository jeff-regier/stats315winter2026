---
## Critique: Groupwork 9 - Kaggle Galaxy Challenge with CNNs

### Issues Requiring Review

#### 1. Problem 3 Split Across Non-Contiguous Cells
**Location:** Cells 25 (optimizer/batch_size) and 28 (data loaders)
**Description:** Problem 3 has solution code split across two separate cells that are not adjacent. Cell 25 contains the optimizer and batch size configuration, while cell 28 contains the data loader setup.
**Why it needs review:** This structure could cause confusion for students and grading. Consider whether to split Problem 3 into two separate problems ("Configure Optimizer and Batch Size" and "Create Data Loaders") and renumber subsequent problems, or consolidate the solutions into a single cell.

#### 2. Solution Hint May Be Too Prescriptive
**Location:** Cell 16 (Problem 1)
**Description:** The hint "Conv -> ReLU -> Pool -> Conv -> ReLU -> Pool -> Flatten -> FC -> ReLU -> FC" essentially gives away the architecture pattern, making the "design" aspect trivial.
**Why it needs review:** This is a pedagogical choice. A more general hint like "Consider stacking convolutional blocks followed by fully connected layers" would encourage more exploration, but the specific hint may be intentional scaffolding for beginners.

#### 3. Solution Complexity Exceeds Requirements
**Location:** Cell 28
**Description:** The solution implements a custom `AugmentedGalaxyDataset` class with data augmentation (random flips and rotations), but the problem statement only asks students to "set up data loaders."
**Why it needs review:** Decide whether to: (a) simplify the solution to use basic `TensorDataset` and `DataLoader`, (b) add data augmentation as an explicit optional extension in the problem description, or (c) keep the advanced solution to demonstrate best practices.

#### 4. Kaggle Competition Link May Expire
**Location:** Cell 1
**Description:** The Kaggle competition link `https://www.kaggle.com/t/c7bb7892c2774d61af49f788398b2eec` uses a temporary invite token format that may expire between semesters.
**Why it needs review:** Verify the link is still active and consider whether to note that the link may need to be updated each semester, or use a permanent competition URL if available.

#### 5. Hardcoded File Paths
**Location:** Cell 7
**Description:** File paths are hardcoded to `data/` which may not match all students' setups, especially those not using Google Colab.
**Why it needs review:** Consider whether to add a note about adjusting paths for different environments, or provide alternative path configurations.

---
