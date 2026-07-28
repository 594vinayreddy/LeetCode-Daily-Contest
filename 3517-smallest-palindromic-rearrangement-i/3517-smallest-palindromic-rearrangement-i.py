class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)

        left = []
        middle = ""

        for ch in map(chr, range(ord('a'), ord('z') + 1)):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        left = "".join(left)

        return left + middle + left[::-1]