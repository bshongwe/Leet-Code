# 🌲 Maximum Path Sum in a Binary Tree
## 📚 Problem Statement

Given the root of a binary tree, find the maximum path sum of any non-empty path. A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can only appear in the sequence at most once. The path sum of a path is the sum of the node's values in the path.

### 📌 Examples

- **Example 1**:
  - **Input**: `root = [1,2,3]`
  - **Output**: `6`
  - **Explanation**: The optimal path is `2 -> 1 -> 3` with a path sum of `2 + 1 + 3 = 6`.

- **Example 2**:
  - **Input**: `root = [-10,9,20,null,null,15,7]`
  - **Output**: `42`
  - **Explanation**: The optimal path is `15 -> 20 -> 7` with a path sum of `15 + 20 + 7 = 42`.

## 🛠️ Solutions

### 🛠️ Solution 1: Basic Approach

#### Approach:
1. **Tree Traversal** 🌲:
   - Use Depth-First Search (DFS) to explore all paths starting from each node.
   - The function recursively calculates the maximum path sum for left and right subtrees.

2. **Path Sum Calculation** 🧮:
   - At each node, calculate the maximum path sum including the node and its left and right children.
   - Consider paths that extend to the left, right, or both children.

3. **Recursive Function** 🔄:
   - Calculates and returns the maximum path sum that can be extended to the parent node.
   - Updates the global maximum path sum.

#### ⏱️ Time Complexity:
- **`O(n)`**: Each node is visited once.

#### 🧩 Space Complexity:
- **`O(h)`**: Space used by the recursion stack, where `h` is the height of the tree.

### 🛠️ Solution 2: Optimized Approach

#### Approach:
1. **Enhanced Calculation** 🔍:
   - Use DFS to compute maximum path sums while efficiently updating the global maximum path sum.
   - Only consider positive contributions from left and right subtrees.

2. **Global Variable** 🌟:
   - Maintain a global variable to track the maximum path sum across all nodes.
   - Update this variable based on the maximum path sums including and extending from each node.

3. **Positive Contributions** ➕:
   - Only positive path sums are considered to avoid reducing the overall path sum.

#### ⏱️ Time Complexity:
- **`O(n)`**: Each node is visited once.

#### 🧩 Space Complexity:
- **`O(h)`**: Space used by the recursion stack, where `h` is the height of the tree.

## 🔍 Comparison Table

| **Aspect**                | **Solution 1**                                                  | **Solution 2**                                                |
|---------------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| **Approach**              | Basic DFS traversal with path sum calculation.                  | Enhanced DFS with efficient global maximum updates.           |
| **Path Sum Calculation**  | Considers all paths including both children and updates maximum path sum. | Focuses on positive contributions and streamlined updates.    |
| **Handling Negative Values** | May not handle negative values optimally.                        | Handles negative values more effectively by considering positive contributions. |
| **Global Variable**       | Uses global variable to track maximum path sum.                  | Uses global variable for efficient maximum path sum updates.   |
| **Time Complexity**       | `O(n)`                                                            | `O(n)`                                                         |
| **Space Complexity**      | `O(h)` (recursion stack)                                         | `O(h)` (recursion stack)                                      |

## 🏆 Conclusion

Both solutions effectively solve the problem of finding the maximum path sum in a binary tree. Solution 1 provides a straightforward implementation, while Solution 2 offers optimizations that handle negative values and streamline path sum calculations. Both solutions ensure robust performance for large trees within the given constraints.

For further reading and problem-solving, you may refer to:
- [LeetCode Problem](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [Tree Traversal Techniques](https://en.wikipedia.org/wiki/Tree_traversal)

