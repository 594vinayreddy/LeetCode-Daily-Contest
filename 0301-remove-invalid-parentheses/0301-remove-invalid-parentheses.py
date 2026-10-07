class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = r = 0
        for ch in s:
            if ch == "(":
                l += 1
            elif ch == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1

        def is_valid(t):
            bal = 0
            for ch in t:
                if ch == "(":
                    bal += 1
                elif ch == ")":
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        res = []

        def dfs(start, t, l, r):
            if l == 0 and r == 0:
                if is_valid(t):
                    res.append(t)
                return
            
            for i in range(start, len(t)):
                if i > start and t[i] == t[i - 1]:
                    continue
                if t[i] == "(" and l > 0:
                    dfs(i, t[:i] + t[i + 1:], l - 1, r)
                elif t[i] == ")" and r > 0:
                    dfs(i, t[:i] + t[i + 1:], l, r - 1)
        dfs(0, s, l, r)
        return res
