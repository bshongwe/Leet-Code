# 🧩 Generate Parentheses
## 📝 Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### 📌 Example 1:
- **Input**: `n = 3`
- **Output**: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

### 📌 Example 2:
- **Input**: `n = 1`
- **Output**: `["()"]`

## 💡 Approach

The challenge is to generate all valid combinations of parentheses using `n` pairs. We'll use a backtracking approach:

1. **Backtracking** 🌀:
   - Generate strings by placing an opening `(` or a closing `)` parenthesis at each step.
   - Add `(` if there are any left to use.
   - Add `)` if it won't close more than it opens.

2. **Base Case**:
   - When the string reaches a length of `2 * n`, it's a valid combination.

3. **Recursive Exploration** 🔄:
   - Explore adding `(` and `)` while maintaining the balance between them.

### 🚀 Example Usage:

```python
# Example 1
sol = Solution()
print(sol.generateParenthesis(3))  
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2
print(sol.generateParenthesis(1))  
# Output: ["()"]
```

## 📊 Complexity Analysis

- **Time Complexity**: The time complexity is `O(4^n / sqrt(n))`, as there are `Catalan(n)` combinations, and generating each combination takes linear time.
- **Space Complexity**: The space complexity is `O(4^n / sqrt(n))` to store all combinations.

## 🔗 References

- [LeetCode Problem](https://leetcode.com/problems/generate-parentheses/)
- [Backtracking Explained](https://en.wikipedia.org/wiki/Backtracking)

## 👏 Conclusion

This problem is a classic example of generating combinatorial objects with constraints. The backtracking approach is efficient and easy to understand for generating valid parentheses combinations.
