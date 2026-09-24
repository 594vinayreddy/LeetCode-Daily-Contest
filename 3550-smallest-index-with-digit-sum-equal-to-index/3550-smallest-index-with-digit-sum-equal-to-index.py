class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def digitSum(num):
            add = 0
            while num > 0:
                rem = num % 10
                num = num // 10
                add += rem
            return add

        for i in range(n):
            if digitSum(nums[i]) == i:
                return i
        else:
            return -1