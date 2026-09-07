class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        end = {}
        total = 0

        for c in s:
            new_end_c = (total + 1) % MOD
            total = (total - end.get(c, 0) + new_end_c) % MOD
            end[c] = new_end_c
        
        return total % MOD
            