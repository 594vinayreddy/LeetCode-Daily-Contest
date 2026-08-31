class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0 for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            lgt = 0
            maxi = float("-inf")
            max_ans = float("-inf")
            for j in range(i, min(n, i + k)):
                lgt += 1
                maxi = max(maxi, arr[j])
                sum = (lgt * maxi) + dp[j + 1]
                max_ans = max(max_ans, sum)
            dp[i] = max_ans  
        return dp[0]