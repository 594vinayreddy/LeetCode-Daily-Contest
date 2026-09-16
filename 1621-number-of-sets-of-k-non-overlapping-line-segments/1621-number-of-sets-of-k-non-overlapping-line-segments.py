class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        N = n + k - 1   
        r = 2 * k       

        numerator = 1
        for i in range(r):
            numerator = numerator * (N - i) % MOD

        denominator = 1
        for i in range(1, r + 1):
            denominator = denominator * i % MOD

        return numerator * pow(denominator, MOD - 2, MOD) % MOD