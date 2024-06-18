# LeetCode Challenge 18: 4Sum 🔢➕➕➕
## Description 📝
The **4Sum** problem involves finding all unique quadruplets in an array that sum up to a given target. The quadruplets should be returned in any order, and the solution should ensure no duplicates are included.

## Problem Statement ❓
Given an array `nums` of `n` integers, return an array of all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- `0 <= a, b, c, d < n`
- `a, b, c, and d are distinct`
- `nums[a] + nums[b] + nums[c] + nums[d] == target`
<br></br>
### Examples 📚
#### Example 1
- **Input**: `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`
- **Output**: `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`
- **Explanation**: The quadruplets that sum to 0 are returned.

#### Example 2
- **Input**: `nums = [2, 2, 2, 2, 2]`, `target = 8`
- **Output**: `[[2, 2, 2, 2]]`
- **Explanation**: The only quadruplet that sums to 8 is returned.

#### Constraints ⚠️
- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

# Solution Approach 🛠️
The solution uses a combination of sorting and the two-pointer technique to efficiently find all unique quadruplets:

1. **Sort the Array**: Sorting helps in managing duplicates and using the two-pointer technique effectively.
2. **Fix Two Numbers**: Use two nested loops to fix the first two numbers in the quadruplet.
3. **Two-Pointer Technique**: Use two pointers to find the remaining two numbers that sum up to the target.
4. **Skip Duplicates**: Ensure that no duplicate quadruplets are included by skipping over repeated elements.

### Implementation 💻
I used a Python3 script
<br></br>
### Example usage:
```
solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(solution.fourSum([2, 2, 2, 2, 2], 8))       # Output: [[2,2,2,2]]
```
<br></br>
### Explanation 📖
1. **Sorting**: The input array `nums` is sorted to facilitate the two-pointer technique and to manage duplicates easily.
2. **Nested Loops for First Two Numbers**: Two nested loops are used to fix the first two numbers. The outer loop runs from `0` to `n-3` and the inner loop runs from `i+1` to `n-2`.
3. **Two-Pointer Technique**: For the remaining two numbers, two pointers (`left` and `right`) are used. The `left` pointer starts just after the second fixed number (`j+1`), and the `right` pointer starts at the end of the array.
4. **Checking Sum and Skipping Duplicates**: If the sum of the four numbers matches the target, the quadruplet is added to the result list. Duplicates are skipped by moving the pointers past any identical elements.
5. **Adjusting Pointers**: Depending on whether the current sum is less than or greater than the target, the `left` or `right` pointer is adjusted respectively.

This approach efficiently finds all unique quadruplets that sum up to the target and ensures no duplicates are included in the result list. The time complexity is \(O(n^3)\), making it suitable for the given constraints.

## License ⚖️
TBA
