class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        after = [[0 for _ in range(k + 1)] for _ in range(2)]

        for i in range(n - 1, -1, -1):
            curr = [[0 for _ in range(k + 1)] for _ in range(2)]
            for buy in range(0, 2):
                for limit in range(1, k + 1):
                    if buy:
                        profit = max(-prices[i] + after[0][limit], after[1][limit])
                    else:
                        profit = max(prices[i] + after[1][limit - 1], after[0][limit])
                    curr[buy][limit] = profit
            after = curr
        return after[1][k]
