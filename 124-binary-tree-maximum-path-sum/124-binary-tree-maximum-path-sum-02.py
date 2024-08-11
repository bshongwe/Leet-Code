class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0

            # Compute the maximum path sum of the left and right subtrees
            left_max = max(helper(node.left), 0)  # Only consider positive contributions
            right_max = max(helper(node.right), 0)  # Only consider positive contributions

            # Calculate the maximum path sum including the current node
            current_max = node.val + left_max + right_max

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_max)

            # Return the maximum path sum that can be extended to the parent
            return node.val + max(left_max, right_max)

        self.max_sum = float('-inf')  # Initialize with the smallest value
        helper(root)
        return self.max_sum
