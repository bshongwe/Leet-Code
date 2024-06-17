# 🎯 Leet Code Challenge 16: 3Sum Closest

## 📖 Description
The **3Sum Closest** problem is a common algorithmic challenge where, given an integer array `nums` of length `n` and an integer `target`, the goal is to find three integers in `nums` such that the sum is closest to `target`. The function returns the sum of these three integers. You may assume that each input has exactly one solution.
<br></br>

## 📝 Problem Statement
Given an integer array `nums` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.
<br></br>

### 🔍 Examples
#### Example 1
- **Input**: `nums = [-1, 2, 1, -4]`, `target = 1`
- **Output**: `2`
- **Explanation**: The sum that is closest to the target is `2` (`-1 + 2 + 1 = 2`).

#### Example 2
- **Input**: `nums = [0, 0, 0]`, `target = 1`
- **Output**: `0`
- **Explanation**: The sum that is closest to the target is `0` (`0 + 0 + 0 = 0`).

### 📋 Constraints
- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`
<br></br>

# 💡 Solution
### 🛠️ Approach
1. **Sort the Array**: Sorting helps in efficiently using the two-pointer technique.
2. **Initialize Variables**: Use a variable to store the closest sum found, initialized to a large value.
3. **Iterate Over the Array**: Use a for-loop to fix one element and then apply the two-pointer technique for the remaining elements.
4. **Two-Pointer Technique**: Adjust pointers to find the closest sum to the target.
5. **Update Closest Sum**: Update the closest sum if a closer sum is found.
6. **Return Result**: Return the closest sum after evaluating all possible triplets.

# 💻 Implementation
I used a Python3 to implement the solution

### ▶️ Usage
```python
# Example usage:
solution = Solution()

nums1 = [-1, 2, 1, -4]
target1 = 1
print(solution.threeSumClosest(nums1, target1))  # Output: 2

nums2 = [0, 0, 0]
target2 = 1
print(solution.threeSumClosest(nums2, target2))  # Output: 0
```
<br></br>
### 📝 Explanation
1. **Sorting**: The array is sorted to facilitate the two-pointer approach.
2. **Initialization**: The `closest_sum` is initialized to a very large value.
3. **Iteration**: The outer loop fixes one element, and the inner while-loop adjusts the left and right pointers to find the best possible sum.
4. **Pointers Adjustment**: Depending on whether the current sum is less than or greater than the target, the left or right pointer is adjusted respectively.
5. **Closest Sum Update**: The closest sum is updated whenever a closer sum is found.
6. **Immediate Return**: If a sum exactly matching the target is found, it is returned immediately as it is the optimal solution.

### ⏱️ Time Complexity
The solution has a time complexity of \(O(n^2)\) due to the nested loops and is efficient enough for the given constraints.

## 📜 License
TBA
