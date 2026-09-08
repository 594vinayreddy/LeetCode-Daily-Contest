class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = len(str(n))

        if m <= 3:
            return 0

        else:
            return n - 999
