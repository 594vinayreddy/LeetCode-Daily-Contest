class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for j in range(i, n + 1):

                max_cost = 0
                for k in range(i, j + 1):
                    cost = nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k -1] + dp[k + 1][j]
                    max_cost = max(max_cost, cost)
                dp[i][j] = max_cost

        return dp[1][n]