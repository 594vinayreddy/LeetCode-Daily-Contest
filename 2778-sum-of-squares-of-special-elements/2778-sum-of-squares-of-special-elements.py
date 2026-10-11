class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for i in range(n):
            if n % (i + 1) == 0:
                ans += (nums[i] * nums[i] )
        
        return ans