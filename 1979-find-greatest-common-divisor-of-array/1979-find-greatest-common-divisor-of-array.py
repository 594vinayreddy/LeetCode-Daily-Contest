class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        min_num = min(nums)
        max_num = max(nums)

        return gcd(min_num, max_num)