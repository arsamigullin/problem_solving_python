from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row = [0] * m
        col = [0] * n

        computers = []

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    computers.append((i, j))
                    row[i] += grid[i][j]
                    col[j] += grid[i][j]
        count = 0

        for i, j in computers:
            if row[i] > 1 or col[j] > 1:
                count += 1

        return count