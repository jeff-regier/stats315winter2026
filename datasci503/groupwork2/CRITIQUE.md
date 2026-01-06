---
## Critique: DATASCI 503, Group Work 2: Bias, Variance, and Irreducible Error

### Issues Requiring Review

#### 1. Data File Path Assumes Canvas Location
**Location:** Problem 2.1, Cell 40
**Description:** The instructions reference "Canvas filepath is `Files > datasets > NHANES`" but the solution code uses `"data/HDL_L.xpt"`. Students have no guidance on the expected local directory structure.
**Why it needs review:** This is a content/pedagogical decision. Options include: (a) add explicit instructions for students to create a `data/` subdirectory, (b) provide a code cell that downloads the data programmatically, or (c) modify the file paths to match Canvas structure. The instructor should decide how data distribution fits with their course workflow.

#### 2. Ambiguous Boss Narrative
**Location:** Task 1, Cell 6
**Description:** The scenario about the "terrible boss" using ChatGPT is informal and potentially confusing. The phrase "Throughout this lab" suggests the task spans the entire assignment, but it's unclear which problems specifically address this goal.
**Why it needs review:** This is a pedagogical/storytelling choice. The narrative may be intentionally informal to engage students, or it may need clarification. The instructor should decide if this framing is effective or if it should be revised.

#### 3. Problem 1.6 Animation Code Complexity
**Location:** Cell 36
**Description:** Students are given extensive animation boilerplate code with only vague instructions about where to "insert implementations." The actual implementation is mostly pre-written with few places for student input.
**Why it needs review:** This is a pedagogical decision about scaffolding. The instructor should decide whether: (a) to simplify the task with static plots, (b) add explicit `# TODO:` comments, or (c) keep the current design if the learning objective is primarily understanding the animation output rather than creating it.

#### 4. Bias Function Naming Convention
**Location:** Problem 1.5, Cell 30
**Description:** The `bias` function returns raw bias (not squared), but the decomposition equation and animation display `Bias^2`. The plotting code squares the result when displaying.
**Why it needs review:** This is intentional design (returning raw bias allows for both signed bias and squared bias calculations), but the naming could confuse students. The instructor should decide if a docstring clarification, function rename to `mean_error`, or additional explanation would help student understanding.

#### 5. MSE Test Tolerance Value
**Location:** Problem 1.5, Cell 33
**Description:** The test `assert np.abs(mse(-5, dgp, model_list) - 282) < 20` uses a wide tolerance (20) that may not be stable across runs due to randomness in the model_list generation.
**Why it needs review:** The instructor should verify this tolerance is appropriate for the expected variance in student submissions, or consider setting a random seed before this specific test for reproducibility.

---
