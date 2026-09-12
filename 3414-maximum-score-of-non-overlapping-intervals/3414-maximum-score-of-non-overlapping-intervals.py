class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        items = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        items = sorted(range(len(intervals)), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in items]

        n = len(intervals)
        k = 4
        dp = [[(0, ())] * (k + 1) for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a[0] > b[0]
            return a[1] < b[1]

        for p in range(n):
            idx = items[p]
            l, r, w = intervals[idx]

            cnt = bisect_left(rs, l, 0, p)
            row_skip = dp[p]
            row_next = dp[p + 1]
            for j in range(k + 1):
                skip = row_skip[j]
                if j >= 1:
                    prev_score, prev_idx = dp[cnt][j - 1]
                    take = (prev_score + w, tuple(sorted(prev_idx + (idx,))))
                    row_next[j] = take if better(take, skip) else skip
                else:
                    row_next[j] = skip
        
        return list(dp[n][k][1])