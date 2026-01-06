---
## Critique: Group Work 10 - Transformers

### Issues Requiring Review

#### 1. Missing Input Validation Guidance for Positional Encoding
**Location:** Problem 4 (Cell 14-15)
**Description:** The problem states `embed_dim` must be even but doesn't guide students on how to handle this or whether to validate it.
**Why it needs review:** Pedagogical decision about whether to add an assertion at the start of the function template to enforce even dimensions, or note in the problem description that students don't need to validate this assumption.

#### 2. Worked Example Uses Approximate Values Without Explanation
**Location:** Problem 1 (Cell 4)
**Description:** The worked example shows `Attention weights = [[0.67, 0.33], [0.33, 0.67]]` without showing the softmax calculation. Students might not understand where these numbers come from.
**Why it needs review:** Pedagogical choice about whether to add the softmax calculation step showing: "softmax([0.707, 0]) = [exp(0.707)/(exp(0.707)+exp(0)), exp(0)/(exp(0.707)+exp(0))] = [0.67, 0.33]"

#### 3. Problem 5 Mask Conversion Could Be Clearer
**Location:** Problem 5 (Cell 18)
**Description:** The instructions mention using `torch.where` to convert the boolean mask but don't provide enough context about why this is needed or a concrete example.
**Why it needs review:** Pedagogical choice about whether to add a brief code snippet showing the conversion pattern to help students understand the mask format conversion.

#### 4. Test Range for Perplexity Is Too Wide
**Location:** Problem 6 (Cell 23)
**Description:** The assertion `perplexity > 50 and perplexity < 200` is a very wide range that might pass incorrect implementations. For a random model with vocab_size=100, the expected perplexity should be closer to 100.
**Why it needs review:** Requires judgment about appropriate test tolerance - tightening to something like `75 < perplexity < 125` could be more principled but might cause false failures depending on random initialization.

#### 5. Problem 3 Lacks Sufficient Scaffolding
**Location:** Problem 3 (Cell 10-11)
**Description:** The problem asks students to "set `causal_attention_weights`" but provides minimal guidance. Students need to understand they should call both `create_causal_mask` and `scaled_dot_product_attention`.
**Why it needs review:** Pedagogical decision about how much scaffolding to provide - could add explicit steps like: (1) Create a causal mask, (2) Call scaled_dot_product_attention with the mask, (3) Store the attention weights.

---
