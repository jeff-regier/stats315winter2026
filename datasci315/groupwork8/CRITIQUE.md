---
## Critique: Group Work 8 - Convolutional Neural Networks with CIFAR-10

### Issues Requiring Review

#### 1. External Image Link May Break
**Location:** Problem 1 (cell-8)
**Description:** The CNN architecture diagram is hosted on an external WordPress site (`https://i0.wp.com/developersbreach.com/wp-content/uploads/2020/08/cnn_banner.png`). External links can become unavailable, breaking the assignment for future students.
**Why it needs review:** Deciding whether to host the image locally (requires checking copyright/licensing), replace it with a custom diagram, or provide a complete textual description instead requires human judgment about content ownership and pedagogical approach.

#### 2. Problem 1 Architecture Specification is Incomplete
**Location:** Problem 1 (cell-8)
**Description:** The problem specifies convolutional layer sizes but omits: (1) max pooling parameters (kernel_size=2, stride=2), (2) fully connected layer sizes (400->120->84->10), (3) activation functions (ReLU). Students must infer these from the external diagram or guess.
**Why it needs review:** This is a pedagogical choice. You may want students to figure out some details from the diagram, or you may prefer to provide complete specifications. The current approach depends on the external image remaining accessible.

#### 3. Missing ReLU Activation Mention in Problem 1
**Location:** Problem 1 (cell-8)
**Description:** The problem mentions "Two convolutional layers followed by max pooling" but doesn't explicitly mention that ReLU activation functions should be applied. The solution uses ReLU after each conv layer and after the first two FC layers.
**Why it needs review:** Pedagogical decision about whether students should infer activation functions from the diagram or be told explicitly.

#### 4. Problem 2 Lacks Guidance on Learning Rate
**Location:** Problem 2 (cell-11)
**Description:** The problem says "Any choice of learning rate is fine for now" but poor choices could prevent students from achieving the 50% accuracy target in Problem 4. The solution uses `lr=0.001, momentum=0.9`.
**Why it needs review:** Pedagogical choice about how much guidance to provide. Consider adding a recommended range (e.g., "A learning rate between 0.001 and 0.01 with momentum around 0.9 works well").

#### 5. Long Training Time Without Warning
**Location:** Problem 3 (cell-14/15)
**Description:** Training 2 epochs on CIFAR-10 with batch_size=4 means 25,000 iterations, which can take several minutes on CPU. Students are not warned about expected runtime.
**Why it needs review:** Consider adding a note like "Training may take 2-5 minutes on CPU. You'll see progress updates every 2000 mini-batches."

#### 6. Small Batch Size Without Explanation
**Location:** Data loading section (cell-4)
**Description:** The `batch_size = 4` is unusually small (typical values are 32-128), which significantly slows training. This appears to be from the original PyTorch tutorial.
**Why it needs review:** Consider increasing batch size to speed up training, or add a comment explaining the choice if it's intentional for educational purposes.

---
