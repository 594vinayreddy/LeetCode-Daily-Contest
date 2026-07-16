class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        prefix_gcd = []
        mx = 0

        for x in nums:
            mx = max(mx, x)
            prefix_gcd.append(gcd(x, mx))
        
        prefix_gcd.sort()

        left = 0
        right = len(prefix_gcd) - 1

        ans = 0

        while left < right:
            ans += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        
        return ans