class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            if dp[i] < m  and word1[i] == word2[m - 1 - dp[i]]:
                dp[i] += 1

        res = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not changed and dp[i + 1] >= m - j - 1:
                res.append(i)
                changed = True
                j += 1
        return res if j == m else []