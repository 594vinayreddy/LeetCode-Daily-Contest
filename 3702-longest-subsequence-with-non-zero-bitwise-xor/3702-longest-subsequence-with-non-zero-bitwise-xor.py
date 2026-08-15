class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_all = 0
        has_non_zero = False

        for num in nums:
            xor_all ^= num
            if num != 0:
                has_non_zero = True

        if not has_non_zero:
            return 0
        if xor_all != 0:
            return len(nums)
        return len(nums) - 1