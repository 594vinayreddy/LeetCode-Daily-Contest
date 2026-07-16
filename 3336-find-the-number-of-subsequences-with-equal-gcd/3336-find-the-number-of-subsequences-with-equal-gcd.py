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
        n = len(nums)
        V = max(nums)

        memo = [[[-1] * (V + 1) for _ in range(V + 1)] for _ in range(n + 1)]
        def solve(i, g1, g2):
            if i == n:
                return 1 if (g1 == g2 and g1 != 0) else 0

            if memo[i][g1][g2] != -1:
                return memo[i][g1][g2]
            
            x = nums[i]

            total = solve(i + 1, g1, g2)
            total += solve(i + 1, gcd(g1, x), g2)
            total += solve(i + 1, g1, gcd(g2, x))
            total  %= MOD

            memo[i][g1][g2] = total
            return total

        return solve(0,0,0)
