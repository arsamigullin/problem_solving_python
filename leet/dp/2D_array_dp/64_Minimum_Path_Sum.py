import math
from typing import List

class Solution1:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = {}
        n = len(grid)
        m = len(grid[0])

        def helper(i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]

            if (i, j) not in dp:
                cur = math.inf
                for dx, dy in [(0, 1), (1, 0)]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < m:
                        cur = min(cur, grid[i][j] + helper(x, y))
                dp[(i, j)] = cur
            return dp[(i, j)]

        return helper(0, 0)

# there is some similarities with 63 and 64
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for j in range(m - 1):
            dp[0][j + 1] = dp[0][j] + grid[0][j + 1]

        for i in range(n - 1):
            dp[i + 1][0] = dp[i][0] + grid[i + 1][0]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[-1][-1]

# without extra space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i - 1][j] + grid[i][j], grid[i][j - 1] + grid[i][j])
        return grid[-1][-1]

# single pass and no extra space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]