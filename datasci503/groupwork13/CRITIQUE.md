---
## Critique: DATASCI 503, Group Work 13: Autoencoders with MNIST

### Issues Requiring Review

#### 1. VAE Training Uses Only 5 Epochs
**Location:** Cell 37
**Description:** The VAE is trained for only 5 epochs (`num_epochs=5`), while the autoencoder in Problem 3 uses 100 epochs. This may result in undertrained models that do not demonstrate the full capabilities of VAEs.
**Why it needs review:** This may be an intentional choice for lab time constraints, or it may need to be increased for meaningful learning. The instructor should decide whether to increase epochs (e.g., to 50) or add a note explaining the time tradeoff.

#### 2. Problem 8 Missing Architecture Guidance
**Location:** Cell 31
**Description:** Problem 8 asks students to implement a VAE but does not specify network architecture dimensions, unlike Problem 2 which provides clear guidance (784 -> 256 -> 128 -> 64 -> latent_dim).
**Why it needs review:** The instructor should decide whether to provide explicit architecture guidance (e.g., "Use 512 -> 256 for encoder, output mu and logvar") or explicitly state that students can choose their own architecture.

#### 3. Missing Shuffling Specification in Problem 1
**Location:** Cell 4
**Description:** The problem does not specify whether DataLoaders should shuffle data. The solution shuffles train_loader but not val_loader and test_loader.
**Why it needs review:** This may be intentionally left for students to discover, or it may need explicit instruction: "The train_loader should shuffle data, while val_loader and test_loader should not."

#### 4. GeeksforGeeks Reference Link
**Location:** Cell 3
**Description:** The autoencoder explanation links to GeeksforGeeks, which may not be the most authoritative source.
**Why it needs review:** The instructor should decide whether to supplement or replace this with more authoritative sources (e.g., PyTorch tutorials, academic references, or course materials).

#### 5. KL Divergence Formula Notation
**Location:** Cell 30
**Description:** The KL divergence formula uses both the variance form and logvar in different places without explicit connection. The implementation uses `logvar` but the formula shows standard deviation.
**Why it needs review:** This may need additional clarification to help students understand how the mathematical notation connects to the implementation.

#### 6. ELBO Loss Sign Convention
**Location:** Cell 30
**Description:** The ELBO formula shows `+ KL` but when optimizing we minimize the negative ELBO (the loss). This sign convention may confuse students.
**Why it needs review:** The instructor should verify the mathematical presentation is clear about whether we are maximizing ELBO or minimizing the loss (negative ELBO).

---
