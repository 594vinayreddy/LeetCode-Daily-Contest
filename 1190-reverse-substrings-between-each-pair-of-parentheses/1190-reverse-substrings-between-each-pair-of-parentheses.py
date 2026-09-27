class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for ch in s:
            if ch == '(':
                stack.append('')
            elif ch == ')':
                top = stack.pop()
                stack[-1] += top[::-1]
            else:
                stack[-1] += ch
        return stack[0]