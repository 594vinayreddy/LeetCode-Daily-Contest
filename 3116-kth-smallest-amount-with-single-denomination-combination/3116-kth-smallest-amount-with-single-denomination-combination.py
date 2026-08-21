class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        n = len(coins)

        def gcd(a, b):
            while b!= 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                        if current_lcm > x:
                            break
                
                else:
                    if bits % 2 == 1:
                        total += x // current_lcm
                    else:
                        total -= x // current_lcm
            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left