# LeetCode Challenge 19: Remove Nth Node From End of List 🗑️🧩
## Description 📝
The **Remove Nth Node From End of List** problem involves removing the nth node from the end of a given linked list and returning the head of the modified list.

### Problem Statement ❓
Given the head of a linked list, remove the nth node from the end of the list and return its head.
<br></br>
### Examples 📚
#### Example 1
- **Input**: `head = [1,2,3,4,5]`, `n = 2`
- **Output**: `[1,2,3,5]`
- **Explanation**: The 2nd node from the end (node with value 4) is removed.

#### Example 2
- **Input**: `head = [1]`, `n = 1`
- **Output**: `[]`
- **Explanation**: The only node in the list is removed.

#### Example 3
- **Input**: `head = [1,2]`, `n = 1`
- **Output**: `[1]`
- **Explanation**: The last node (node with value 2) is removed.

#### Constraints ⚠️
- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

# Solution Approach 🛠️
The solution uses a two-pointer technique to efficiently identify and remove the target node:

1. **Dummy Node**: Introduce a dummy node pointing to the head to handle edge cases seamlessly.
2. **Two Pointers**: Use two pointers, `first` and `second`. Move `first` pointer `n+1` steps ahead.
3. **Simultaneous Movement**: Move both pointers until `first` reaches the end. Now, `second` points to the node just before the target node.
4. **Remove Node**: Adjust `second.next` to skip the target node.

### Implementation 💻
I use a Python3 script

### Example usage:
```
# Create linked list [1, 2, 3, 4, 5]
head = create_linked_list([1, 2, 3, 4, 5])
n = 2
solution = Solution()
new_head = solution.removeNthFromEnd(head, n)
print(linked_list_to_list(new_head))  # Output: [1, 2, 3, 5]
```
<br></br>
### Explanation 📖
1. **Dummy Node**: A dummy node is created to handle edge cases like removing the head node.
2. **First Pointer Advancement**: The `first` pointer is advanced `n+1` steps to create a gap.
3. **Simultaneous Advancement**: Both pointers are moved until `first` reaches the end. `second` then points to the node before the target.
4. **Node Removal**: Adjust `second.next` to skip the target node.
5. **Return Result**: Return the modified list starting from `dummy.next`.

This approach ensures a single traversal of the list, making it efficient with a time complexity of \(O(sz)\), where \(sz\) is the number of nodes in the list.

## License ⚖️
TBA
