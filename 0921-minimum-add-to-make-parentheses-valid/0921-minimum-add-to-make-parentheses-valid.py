class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if not stack or stack[-1] == ch:
                    stack.append(ch)
                else:
                    stack.pop()

        return len(stack)