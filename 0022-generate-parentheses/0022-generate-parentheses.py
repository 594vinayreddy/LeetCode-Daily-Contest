class Solution(object):
    def solve(self, ind, total, brackets, result, n):
        if ind == 2 * n:
            if total == 0:
                result.append("".join(brackets))
            return

        if total < 0 or total > n:
            return

        brackets[ind] = "("
        self.solve(ind + 1, total + 1, brackets, result, n)

        brackets[ind] = ")"
        self.solve(ind + 1, total - 1, brackets, result, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        brackets = [""] * (2 * n)
        result = []
        self.solve(0, 0, brackets, result, n)
        return result
