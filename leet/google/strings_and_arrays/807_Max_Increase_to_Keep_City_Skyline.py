from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowmax = []
        colmax = []
        for row in grid:
            rowmax.append(max(row))

        for col in zip(*grid):
            colmax.append(max(col))
        total = 0
        for i in range(n):
            for j in range(m):
                total += min(rowmax[i], colmax[j]) - grid[i][j]
        return total




class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))