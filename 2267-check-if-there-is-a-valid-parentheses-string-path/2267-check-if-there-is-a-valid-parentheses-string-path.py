class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        n = len(grid)
        m = len(grid[0])

        if (n + m - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[n - 1][m - 1] == '(':
            return False

        memo = {}

        def dfs(i, j, balance):
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            remaining = (n - i - 1) + (m - j - 1)
            if balance > remaining:
                return False

            if i == n - 1 and j == m - 1:
                return balance == 0

            state = (i, j, balance)

            if state in memo:
                return memo[state]

            if j + 1 < m:
                if dfs(i, j + 1, balance):
                    memo[state] = True
                    return True

            if i + 1 < n:
                if dfs(i + 1, j, balance):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0, 0)