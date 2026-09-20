class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i, c in enumerate(s):
            reverse_alpha_value = 26 - (ord(c) - ord('a'))
            total += reverse_alpha_value * (i + 1)
        return total