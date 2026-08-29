class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        ahead = [0] * 2

        for i in range(n-1, -1, -1):
            curr = [0] * 2
            for buy in range(0, 2):
                if buy:
                    profit = max(-prices[i] + ahead[0], 0 + ahead[1])
                else:
                    profit = max(prices[i] + ahead[1], 0 + ahead[0])
            
                curr[buy] = profit
            ahead = curr

        return ahead[1]