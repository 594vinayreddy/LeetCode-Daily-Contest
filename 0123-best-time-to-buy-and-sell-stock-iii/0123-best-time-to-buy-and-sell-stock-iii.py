class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        after = [[0 for _ in range(3)] for _ in range(2)]

        for i in range(n - 1, -1, -1):
            curr = [[0 for _ in range(3)] for _ in range(2)]
            for buy in range(0, 2):
                for limit in range(1, 3):
                    if buy:
                        profit = max(-prices[i] + after[0][limit], after[1][limit])
                    else:
                        profit = max(prices[i] + after[1][limit - 1], after[0][limit])
                    curr[buy][limit] = profit
            after = curr
        return after[1][2]




        # n=len(prices)

        # dp=[[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        # for buy in range(0,2):
        #     for limit in range(0,3):
        #         dp[n][buy][limit]=0

        # for i in range(0,n+1):
        #     for buy in range(0,2):
        #         dp[i][buy][0]=0

        # for i in range(n-1,-1,-1):
        #     for buy in range(0,2):
        #         for limit in range(1,3):
        #             if buy==1:
        #                 buy_p=-prices[i]+dp[i+1][0][limit]
        #                 not_buy=dp[i+1][1][limit]
        #                 profit=max(buy_p,not_buy)

        #             else:
        #                 sell=prices[i]+dp[i+1][1][limit-1]
        #                 not_sell=dp[i+1][0][limit]
        #                 profit=max(sell,not_sell)
        #             dp[i][buy][limit] = profit

        # return dp[0][1][2]
