---
## Critique: Group Work 5 - Galaxy Count Prediction with Neural Networks

### Issues Requiring Review

#### 1. Missing Loss Function Explanation in Problem 2
**Location:** Cell 20 (Problem 2 instructions)
**Description:** The instructions mention using `loss_fn` but never explain what loss function should be used or why cross-entropy is appropriate for multi-class classification.
**Why it needs review:** Adding pedagogical explanation about loss function choice is a content decision that may affect learning outcomes.

#### 2. No Guidance on Expected Training Time
**Location:** Training section (cells 20-27)
**Description:** Students are not given any indication of how long training might take with the suggested hyperparameters, which could cause confusion about whether the model is stuck or working.
**Why it needs review:** Deciding whether to add timing guidance or progress printing involves balancing scaffolding against student self-discovery.

#### 3. Problem 2 Contains Two Distinct Coding Tasks
**Location:** Cells 21 and 24
**Description:** Problem 2 asks students to implement the training loop, but then separately asks them to pick learning rate and batch size in cell 24 (also marked as SOLUTION). These are related but distinct tasks.
**Why it needs review:** Deciding whether to split into Problem 2a/2b or keep combined is a pedagogical structure decision.

#### 4. Galaxy Count Range Not Verified
**Location:** Cell 12
**Description:** States counts range from 0 to 6, but this is not verified or explained how this was determined from the dataset.
**Why it needs review:** Adding data verification or documentation is a content decision about how much context to provide students.

#### 5. Goal Section Lacks Problem Header
**Location:** Cells 31-36
**Description:** The "Goal: Achieve Target Accuracy" section contains test assertions but lacks a formal problem number, making it feel like an implicit "Problem 3".
**Why it needs review:** Deciding whether this should be formally numbered as Problem 3 is a structural decision that may affect grading rubric alignment.

---
