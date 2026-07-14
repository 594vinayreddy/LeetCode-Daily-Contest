class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b=b, a % b
            return a

        MOD = 10**9 + 7
        M = 201
        dp= [[0] * M for _ in range(M)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]
            for g1 in range(M):
                row = dp[g1]
                for g2 in range(M):
                    c = row[g2]
                    if c == 0:
                        continue
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + c) % MOD
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + c) % MOD
            dp = new_dp
        return sum(dp[g][g] for g in range(1, M)) % MOD