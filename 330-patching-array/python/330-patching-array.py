class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        Finds the minimum number of patches needed to form sums from 1 to n.

        Args:
            nums: A sorted list of integers.
            n: The upper limit of the range.

        Returns:
            The minimum number of patches required.
        """
        miss = 1  # Smallest missing sum
        added = 0  # Number of patches added
        i = 0  # Index for nums

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # Can use existing number, update miss
                i += 1
            else:
                added += 1  # Patch needed, add miss itself
                miss += miss  # Update miss by adding itself (largest gap covered)

        return added
