class Solution(object):
    CAP = 10**6 + 1

    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = Counter(s)

        half_count = [0] * 26
        mid_char = ''
        for ch, f in freq.items():
            half_count[ord(ch) - ord('a')] = f // 2
            if f % 2 == 1:
                mid_char = ch

        half_len = sum(half_count)

        total = self._count_arrangements(half_count[:])
        if k > total:
            return ""

        left = []
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                half_count[i] -= 1
                arrangements = self._count_arrangements(half_count[:])
                if arrangements >= k:
                    left.append(chr(ord('a') + i))
                    break
                else:
                    k -= arrangements
                    half_count[i] += 1
        left_str = ''.join(left)
        return left_str + mid_char + left_str[::-1]

    def _count_arrangements(self, counts):
        total = sum(counts)
        res = 1
        for f in counts:
            res *= self._nCk(total, f)
            if res >= self.CAP:
                return self.CAP
            total -= f
        return res

    def _nCk(self, n, k):
        k = min(k, n - k)
        res = 1
        for i in range(1, k + 1):
            res = res * (n - k + i) // i
            if res >= self.CAP:
                return self.CAP
        return res