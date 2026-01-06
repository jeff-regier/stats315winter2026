---
## Critique: DATASCI 315, Group Work 12: Los Angeles Traffic Prediction with Graph Neural Networks

### Issues Requiring Review

#### 1. External Repository Dependency Without Version Pinning
**Location:** Cell 6 (cloning stgat_traffic_prediction repo)
**Description:** The assignment clones `https://github.com/jswang/stgat_traffic_prediction` without specifying a commit hash or tag. No fallback instructions exist if the clone fails.
**Why it needs review:** If the repository is modified, moved, or deleted, the entire assignment breaks. Decide whether to: (a) pin to a specific commit, (b) fork the repository under course control, (c) add error handling and troubleshooting instructions, or (d) accept the risk as-is for a live course.

#### 2. Working Directory Change Pattern
**Location:** Cell 6 (`os.chdir(repo_path)`)
**Description:** The notebook changes the working directory without restoration. This can cause issues if cells are run out of order.
**Why it needs review:** This is a design pattern choice. Options include: (a) keep as-is with a note about cell execution order, (b) restructure to use absolute paths throughout, or (c) add a cell to reset the working directory. The current approach matches how Colab notebooks typically operate.

#### 3. GPU Requirement Clarity
**Location:** Cell 1 (instructions) and Cell 3-4 (GPU check)
**Description:** Instructions say GPU "would be helpful" but training 60 epochs on CPU is likely impractical. No guidance is provided for students without GPU access.
**Why it needs review:** Decide whether to: (a) state GPU is required, (b) reduce epochs for CPU fallback, (c) provide estimated training times, or (d) accept that this is a Colab-focused assignment where GPU is typically available.

#### 4. Deprecated resize_() API Usage
**Location:** Cell 8 (TrafficDataset.process method)
**Description:** The code uses `tensor.resize_()` which is deprecated in PyTorch. Modern approach would use slicing: `edge_index = edge_index[:, :num_edges]`.
**Why it needs review:** This code is in provided infrastructure (not student code). Changing it may deviate from the original reference implementation. Decide whether to update for modern PyTorch or maintain alignment with the source paper's implementation.

#### 5. Visible Test Reveals Exact Answer for Problem 2a
**Location:** Cell 27 (Problem 2a test assertions)
**Description:** The visible assertion states "A linear graph 0-1-2-3 should have 6 directed edges", which tells students the exact edge count to produce.
**Why it needs review:** This may be intentional scaffolding for an introductory graph problem. Decide whether to: (a) keep as-is for educational guidance, (b) move the specific count to hidden tests, or (c) make the visible test more general (e.g., check connectivity only).

---
