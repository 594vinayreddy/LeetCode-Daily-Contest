class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0      
        need = 0     

        i, n = 0, len(s)
        while i < n:
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    ans += 1
                    need -= 1
            else: 
                need -= 1
                if need == -1:
                    ans += 1
                    need = 1
            i += 1

        return ans + need