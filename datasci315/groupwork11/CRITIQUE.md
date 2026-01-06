---
## Critique: DATASCI 315, Group Work 11: LLM Few-Shot Learning and Fine-Tuning

### Issues Requiring Review

#### 1. Python 3.10+ Requirement for `strict=True` in zip
**Location:** Cell 41 (compute_metrics function)
**Description:** The `strict=True` parameter in `zip(decoded_preds, decoded_labels, strict=True)` requires Python 3.10+.
**Why it needs review:** Decision needed on whether to document the Python version requirement or remove `strict=True` for broader compatibility.

#### 2. Hardcoded Data File Paths Without Existence Check
**Location:** Cells 31, 35
**Description:** The code assumes files exist at `./data/grammar_train.json`, etc. without checking or providing helpful error messages.
**Why it needs review:** Pedagogical decision on whether to add file existence checks, programmatic download, or keep the current approach that requires manual file placement.

#### 3. Weak Test Assertions for Problem 1
**Location:** Cell 26
**Description:** The test only checks that `few_shot_prompt` exists and has >50 characters. It doesn't verify the prompt has examples, proper structure, or that the model was actually run.
**Why it needs review:** Decision needed on how rigorously to test an open-ended creative problem while maintaining flexibility for student creativity.

#### 4. Problem 2 BLEU Threshold Not Verified Programmatically
**Location:** After Cell 70
**Description:** The assignment requires BLEU >= 0.9 but this is not verified by an assertion in the test cells.
**Why it needs review:** Decision needed on whether to add a programmatic assertion for the BLEU threshold, and what the appropriate threshold value should be.

#### 5. No Documentation Links for Key Concepts
**Location:** Throughout
**Description:** Complex concepts (T5, BLEU, few-shot learning, fine-tuning) are introduced without links to documentation or further reading.
**Why it needs review:** Content decision on which resources to link (Hugging Face T5 docs, original T5 paper, BLEU metric explanation, etc.).

#### 6. T5Tokenizer May Show Deprecation Warnings
**Location:** Cells 11, 46, 65
**Description:** `T5Tokenizer` may show deprecation warnings suggesting `T5TokenizerFast` in newer versions of transformers.
**Why it needs review:** Decision needed on whether to switch to `T5TokenizerFast` or document expected warnings.

#### 7. Complete Hyperparameters Provided in Problem 2 Solution
**Location:** Cell 56
**Description:** The solution provides complete working hyperparameters, making it easy to achieve the goal without experimentation.
**Why it needs review:** Pedagogical decision on whether to provide partial solution, ranges, or keep complete values.

#### 8. Different Models Used Without Explanation
**Location:** Cells 11 vs 46
**Description:** Part 1 uses `flan-t5-base` while Part 2 uses `t5-small` without explaining the difference or trade-offs.
**Why it needs review:** Decision needed on whether to add explanation of model choices or standardize on one model family.

---
