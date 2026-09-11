class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        ans = 0

        for u in [0, 2, 4, 6, 8]:
            if freq[u] == 0:
                continue

            freq[u] -= 1

            for h in range(1, 10):
                if freq[h] == 0:
                    continue
                freq[h] -= 1

                ans += sum(1 for d in range(10) if freq[d] > 0)

                freq[h] += 1
            freq[u] += 1
        return ans