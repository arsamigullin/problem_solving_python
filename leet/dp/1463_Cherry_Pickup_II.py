import math


class Solution:
    def cherryPickup(self, grid) -> int:

        memo = {}
        n = len(grid)
        m = len(grid[0])

        def helper(row, col1, col2):

            if (row, col1, col2) not in memo:
                result = 0
                res = -math.inf
                result += grid[row][col1]
                if col1 != col2:
                    result += grid[row][col2]
                if row != n - 1:
                    for column1 in (col1, col1 - 1, col1 + 1):
                        for column2 in (col2, col2 - 1, col2 + 1):
                            if 0 <= column1 < m and 0 <= column2 < m:
                                res = max(res, helper(row + 1, column1, column2))
                    result += res
                memo[(row, col1, col2)] = result
            return memo[(row, col1, col2)]

        return helper(0, 0, m - 1)


class Solution:
    def cherryPickup(self, grid) -> int:

        n = len(grid)
        m = len(grid[0])

        dp = [[[0] * m for _ in range(m)] for __ in range(n)]
        for i in reversed(range(n)):
            for col1 in range(m):
                for col2 in range(m):
                    result = 0
                    cur = 0
                    result += grid[i][col1]
                    if col1 != col2:
                        result += grid[i][col2]
                    if i != n - 1:
                        for new_col1 in [col1, col1 + 1, col1 - 1]:
                            for new_col2 in [col2, col2 + 1, col2 - 1]:
                                if 0 <= new_col1 < m and 0 <= new_col2 < m:
                                    cur = max(cur, dp[i + 1][new_col1][new_col2])
                    result += cur
                    dp[i][col1][col2] = result
        return dp[0][0][m - 1]