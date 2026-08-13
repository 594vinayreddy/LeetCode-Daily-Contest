class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        s = list(s)
        n = len(s)
        size = 1
        while size < n:
            size *= 2

        LC = [''] * (2 * size)
        RC = [''] * (2 * size)
        LL = [0] * (2 * size)
        RL = [0] * (2 * size)
        ML = [0] * (2 * size)
        SZ = [0] * (2 * size)

        def merge(i):
            l, r = 2 * i, 2 * i + 1
            if SZ[l] == 0:
                LC[i], RC[i], LL[i], RL[i], ML[i], SZ[i] = LC[r], RC[r], LL[r], RL[r], ML[r], SZ[r]
                return
            if SZ[r] == 0:
                LC[i], RC[i], LL[i], RL[i], ML[i], SZ[i] = LC[l], RC[l], LL[l], RL[l], ML[l], SZ[l]
                return
            SZ[i] = SZ[l] + SZ[r]
            LC[i], RC[i] = LC[l], RC[r]
            boundary = (RC[l] == LC[r])
            LL[i] = LL[l] + (LL[r] if boundary and LL[l] == SZ[l] else 0)
            RL[i] = RL[r] + (RL[l] if boundary and RL[r] == SZ[r] else 0)
            mid = (RL[l] + LL[r]) if boundary else 0
            ML[i] = max(ML[l], ML[r], mid)

        for idx, ch in enumerate(s):
            i = size + idx
            LC[i] = RC[i] = ch
            LL[i] = RL[i] = ML[i] = SZ[i] = 1
        for i in range(size - 1, 0, -1):
            merge(i)

        def update(pos, ch):
            i = size + pos
            LC[i] = RC[i] = ch
            i //= 2
            while i >= 1:
                merge(i)
                i //= 2

        result = []
        for c in range(len(queryIndices)):
            pos, ch = queryIndices[c], queryCharacters[c]
            s[pos] = ch
            update(pos, ch)
            result.append(ML[1])
        return result