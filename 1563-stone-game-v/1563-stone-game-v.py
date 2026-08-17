class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def rsum(a, b):
            return prefix[b + 1] - prefix[a]

        dp = [[0] * n for _ in range(n)]
        maxLeft = [[0] * n for _ in range(n)]  
        maxRight = [[0] * n for _ in range(n)] 

        for i in range(n):
            maxLeft[i][i] = stoneValue[i]
            maxRight[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                lo, hi, k0 = i, j - 1, i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if rsum(i, mid) <= rsum(mid + 1, j):
                        k0 = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                leftVal = maxLeft[i][k0] if k0 >= i else 0
                eq = k0 >= i and rsum(i, k0) == rsum(k0 + 1, j)
                rightStart = (k0 + 1) if eq else (k0 + 2)
                rightVal = maxRight[rightStart][j] if rightStart <= j else 0

                dp[i][j] = max(leftVal, rightVal)
                maxLeft[i][j] = max(maxLeft[i][j - 1], dp[i][j] + rsum(i, j))
                maxRight[i][j] = max(maxRight[i + 1][j], dp[i][j] + rsum(i, j))

        return dp[0][n - 1]