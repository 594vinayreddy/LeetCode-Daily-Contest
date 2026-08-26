class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        positions = []

        for i in range(len(s)):
            if s[i] == "1":
                positions.append(i)
            
        if len(positions) < k:
            return ""
        
        ans = ""

        for i in range(len(positions) - k + 1):
            left = positions[i]
            right = positions[i + k - 1]

            current = s[left:right + 1]

            if ans == "":
                ans = current
            elif len(current) < len(ans):
                ans = current
            elif len(current) == len(ans) and current < ans:
                ans = current
        return ans