# Challenge 1: Two Sum ➕

## Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example

### Example 1:
Input: `nums = [2,7,11,15], target = 9`
Output: `[0,1]`
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. ✅

### Example 2:
Input: `nums = [3,2,4], target = 6`
Output: `[1,2]`
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2]. ✅

### Example 3:
Input: `nums = [3,3], target = 6`
Output: `[0,1]`
Explanation: Because nums[0] + nums[1] == 6, we return [0, 1]. ✅

## Constraints
- `2 <= nums.length <= 10^4` 📝
- `-10^9 <= nums[i] <= 10^9` 🔢
- `-10^9 <= target <= 10^9` 🎯
- Only one valid answer exists. ✔️

## Solution 1:
- **Input Parameters**: The function `twoSum` takes in an integer array `nums`, its size `numsSize`, target sum `target`, and a pointer `returnSize` to set the size of the returned array.
- **Looping Strategy**: It uses nested loops (`i` and `j`) to iterate through possible pairs of indices in the `nums` array.
- **Condition Check**: Checks if the sum of elements at indices `i` and `j` equals `target`.
- **Memory Allocation**: If a solution is found, it allocates memory (`malloc`) for a new integer array `res` of size 2, stores `i` and `j` in `res`, and returns `res`.
- **Failure Case**: If no solution is found after iterating through all pairs, it sets `*returnSize` to 0 and returns `NULL`.
