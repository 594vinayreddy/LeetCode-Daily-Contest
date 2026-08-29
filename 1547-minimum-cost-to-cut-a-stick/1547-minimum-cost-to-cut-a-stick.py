class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """

        cuts.sort()
        cuts = [0] + cuts + [n]

        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        def dfs(l, r):
            if r - l <= 1:
                return 0

            if dp[l][r] != 0:
                return dp[l][r]

            result = float("inf")

            for k in range(l + 1, r):
                cost = (
                    cuts[r] - cuts[l]
                    + dfs(l, k)
                    + dfs(k, r)
                )

                result = min(result, cost)

            dp[l][r] = result
            return result

        return dfs(0, m - 1)