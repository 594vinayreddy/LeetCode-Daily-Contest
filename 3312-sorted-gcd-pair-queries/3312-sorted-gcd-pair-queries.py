from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        M = max(nums)
        cnt = [0] * (M + 1)
        for x in nums:
            cnt[x] += 1

        multiple = [0] * (M + 1)
        for d in range(1, M + 1):
            s = 0
            for k in range(d, M + 1, d):
                s += cnt[k]
            multiple[d] = s

        atLeast = [m * (m - 1) // 2 for m in multiple]

        exact = [0] * (M + 2)
        for d in range(M, 0, -1):
            s = atLeast[d]
            k = 2 * d
            while k <= M:
                s -= exact[k]
                k += d
            exact[d] = s

        prefix = [0] * (M + 1)
        running = 0
        for d in range(1, M + 1):
            running += exact[d]
            prefix[d] = running

        ans = []
        for q in queries:
            d = bisect_right(prefix, q)   
            ans.append(d)
        return ans