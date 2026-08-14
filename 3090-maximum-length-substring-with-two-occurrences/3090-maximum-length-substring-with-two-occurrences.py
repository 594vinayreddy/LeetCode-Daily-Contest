class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_dict = defaultdict(int)
        i = 0
        max_len = 0

        for j in range(len(s)):
            freq_dict[s[j]] += 1
            if freq_dict[s[j]] > 2:
                while freq_dict[s[j]] > 2:
                    freq_dict[s[i]] -= 1
                    i += 1
            else:
                max_len = max(max_len, j - i + 1)
        
        return max_len