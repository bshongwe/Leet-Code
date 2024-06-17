## 330. Patching Array Challenge  
This code solves the minimum patches challenge, where the goal is to find the minimum number of elements you need to add to a sorted integer array    such that any number in the range [1, n] can be formed by the sum of elements in the array ➕. 
<br></br>

### Problem Description 
Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array  ️  such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required . 
<br></br>
**Imagine you have a collection of coins, represented by the elements in `nums`. You want to be able to form any amount of money from 1 to `n` using these coins. However, you can also add a few extra coins (patches) to your collection  . The challenge is to find the minimum number of extra coins (patches) you need to add so that you can form any amount from 1 to `n` using the combined coins (original + patches).**
</br></br>

### Examples  
```
Example 1:
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
```
<br></br>
```
Example 2:
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
```
<br></br>
```
Example 3:
Input: nums = [1,2,2], n = 5
Output: 0
```

### Solution Approach 

The solution utilizes a greedy approach  . We iterate through the array and keep track of the smallest sum (`miss`) that cannot be formed from the existing elements. If the current element in the array is less than or equal to `miss`, we can use it to form sums and update `miss`. Otherwise, a patch is needed . We add `miss` itself as a patch, as it represents the largest gap we can cover with a single element .


### Examples  ✨
```
print(Solution().minPatches([1, 3], 6))  # Output: 1
print(Solution().minPatches([1, 5, 10], 20))  # Output: 2
print(Solution().minPatches([1, 2, 2], 5))  # Output: 0
```

### Complexity  
- Time Complexity: O(n), where n is the length of the `nums` array.
- Space Complexity: O(1), as we use constant extra space for variables.
