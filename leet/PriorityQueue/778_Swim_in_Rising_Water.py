import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        res = 0
        while heap:
            dist, x, y = heapq.heappop(heap)
            res = max(res, dist)
            if x == n - 1 and y == n - 1:
                return res
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < n and grid[i][j] > -1:
                    heapq.heappush(heap, (grid[i][j], i, j))
                    grid[i][j] = -1
        return res



