from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')

        zero_groups = []
        group_id = [-1] * n
        for i in range(n):
            if s[i] == '0':
                if i > 0 and s[i - 1] == '0':
                    start, length = zero_groups[-1]
                    zero_groups[-1] = (start, length + 1)
                else:
                    zero_groups.append((i, 1))
            group_id[i] = len(zero_groups) - 1

        if not zero_groups:                      
            return [total_ones] * len(queries)

        m = len(zero_groups)
        pair_sum = [zero_groups[i][1] + zero_groups[i + 1][1] for i in range(m - 1)]

        n_ps = len(pair_sum)
        st = [pair_sum[:]]
        k = 1
        while (1 << k) <= n_ps:
            half = 1 << (k - 1)
            length = n_ps - (1 << k) + 1
            row = [max(st[k - 1][j], st[k - 1][j + half]) for j in range(length)]
            st.append(row)
            k += 1

        def range_max(l: int, r: int) -> int: 
            k = (r - l + 1).bit_length() - 1
            return max(st[k][l], st[k][r - (1 << k) + 1])

        answer = []
        for l, r in queries:
            gid_l, gid_r = group_id[l], group_id[r]

            left_rem = -1
            if s[l] == '0':
                gstart, glen = zero_groups[gid_l]
                left_rem = glen - (l - gstart)

            right_rem = -1
            if s[r] == '0':
                gstart, glen = zero_groups[gid_r]
                right_rem = r - gstart + 1

            start_full = gid_l + 1                        
            end_full = gid_r if s[r] == '1' else gid_r - 1  

            best = total_ones

            if s[l] == '0' and s[r] == '0' and gid_l + 1 == gid_r:
                best = max(best, total_ones + left_rem + right_rem)

            if start_full <= end_full - 1:
                best = max(best, total_ones + range_max(start_full, end_full - 1))

            if s[l] == '0' and start_full <= end_full:
                best = max(best, total_ones + left_rem + zero_groups[start_full][1])

            if s[r] == '0' and gid_l < end_full:
                best = max(best, total_ones + right_rem + zero_groups[end_full][1])

            answer.append(best)

        return answer