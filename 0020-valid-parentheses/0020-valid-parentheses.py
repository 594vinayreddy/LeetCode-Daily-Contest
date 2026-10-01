class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            
            if ch == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()

            elif ch == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()

            if ch == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
        
        return len(stack) == 0