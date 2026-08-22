class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = list(str(n))

        add = 0
        product = 1

        for num in nums:
            num = int(num)
            add += num
            product *= num
        
        return n % (add + product) == 0