---
## Critique: DATASCI 315, Homework 9: Convolutional Neural Networks

### Issues Requiring Review

#### 1. Flowchart images hosted on Google Drive may become inaccessible
**Location:** Cells 14, 17, 20, 31 (Problems 3, 4, 6)
**Description:** The flowchart images use Google Drive URLs (`https://drive.google.com/uc?id=...`). These may require authentication or become unavailable if sharing settings change.
**Why it needs review:** Hosting decision requires evaluating alternatives (repository-hosted images, text descriptions as fallbacks). Students cannot complete Problems 3, 4, and 6 without these architecture diagrams.

#### 2. MysteryBlock solution may not match flowchart
**Location:** Cell 18 (Problem 3)
**Description:** The solution uses `self.pool1` twice with MaxPool2d kernel_size=3. Without viewing the flowchart, it's unclear if this matches the intended architecture. The pooling calculations assume stride=3, but MaxPool2d defaults to kernel_size as stride when not specified.
**Why it needs review:** Requires human to verify the solution matches the flowchart image. The visible test only checks one specific output value which could pass with incorrect implementations.

#### 3. Problem 3 lacks text description of architecture
**Location:** Cell 17 (Problem 3)
**Description:** The problem only shows an image and says "fill in using the following flowchart." There is no text description of what layers are expected (number of conv layers, pooling type, filter sizes, etc.).
**Why it needs review:** Pedagogical decision about whether to add text fallback for accessibility and clarity, or keep image-only to encourage students to read diagrams.

#### 4. Problem 4 has incomplete specification for filters parameter
**Location:** Cell 20 (Problem 4)
**Description:** The problem mentions `filters` is a "List of filter counts" but doesn't explain what happens when `self_conv=False` (2 filters) vs `self_conv=True` (3 filters). The relationship between filter list length and `self_conv` is implicit.
**Why it needs review:** Pedagogical choice about how explicit to make the specification. Could add: "When `self_conv=False`, `filters` should have 2 elements [f1, f2]. When `self_conv=True`, `filters` should have 3 elements [f1, f2, f3] where f3 is for the skip connection conv layer."

#### 5. No PyTorch documentation links provided
**Location:** Throughout the assignment
**Description:** The assignment introduces several PyTorch concepts (nn.Module, Conv2d, BatchNorm2d, MaxPool2d, etc.) but provides no links to official PyTorch documentation.
**Why it needs review:** Pedagogical decision about whether to include documentation links for nn.Conv2d, nn.BatchNorm2d, and transforms module.

#### 6. Training code hardcodes CUDA with no CPU fallback
**Location:** Cells 27, 34-37
**Description:** The `train()` function hardcodes `.cuda()` calls. Students without GPU access cannot run training.
**Why it needs review:** Infrastructure decision about whether to make code device-agnostic (`device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`) or provide Google Colab GPU setup instructions.

#### 7. Hidden tests in Problem 3 only check shape
**Location:** Cell 19 (Problem 3 test cell)
**Description:** The hidden test only checks output shape for a different input size. It doesn't verify internal layer structure or that the architecture matches the flowchart.
**Why it needs review:** Test quality decision about whether to add isinstance checks for layer types, parameter count verification, or intermediate output tests.

#### 8. Inconsistent weight initialization requirements across problems
**Location:** Problems 3, 4, 6
**Description:** Problems 3 and 4 specify weight initialization with std=0.05, but Problem 6 doesn't mention whether to initialize the initial conv layer in ResNet18 (ResidualBlocks have their own initialization).
**Why it needs review:** Pedagogical decision about whether to clarify that only ResidualBlock layers need custom initialization, or require explicit initialization for all conv layers.

#### 9. ResNet18 uses plain list instead of nn.ModuleList for blocks
**Location:** Cell 32 (Problem 6 solution)
**Description:** The `self.blocks` attribute is a plain Python list, not `nn.ModuleList`. However, the blocks are also assigned as named attributes (self.resnetblock_1, etc.), so parameters are still registered.
**Why it needs review:** While technically functional, using `nn.ModuleList` would be more idiomatic. Decide if this should be corrected for educational purposes or left as-is since it works.

#### 10. CIFAR-10 dataset description could be more precise
**Location:** Cell 23
**Description:** The markdown says "60,000 color images" which is the total dataset, but doesn't mention the actual split is 50,000 train / 10,000 test.
**Why it needs review:** Content accuracy decision about whether to add the train/test split detail.

---
