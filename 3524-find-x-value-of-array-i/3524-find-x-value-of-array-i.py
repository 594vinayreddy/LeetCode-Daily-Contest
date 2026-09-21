class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            new_dp[num % k] += 1

            for r in range(k):
                new_r = (r * num) % k
                new_dp[new_r] += dp[r]
            
            for r in range(k):
                ans[r] += new_dp[r]
            
            dp = new_dp
        
        return ans