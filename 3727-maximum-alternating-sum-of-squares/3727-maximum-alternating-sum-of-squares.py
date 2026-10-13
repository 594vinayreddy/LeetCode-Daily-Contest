class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squares = sorted(x * x for x in nums)
        n = len(nums)
        sub = sum(squares[: n // 2])  
        add = sum(squares[n // 2 :])   
        return add - sub