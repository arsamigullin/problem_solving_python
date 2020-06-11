from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        max_val = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            # mark as visited
            visited[i][j] = 1
            path = set()
            cur_max = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and visited[x][y] == 0 and grid[x][y] != 0:
                    val, p = dfs(x, y)
                    if val > cur_max:
                        cur_max = val
                        path = p
            # unmark it back, since we want other nodes to visit all possible paths
            visited[i][j] = 0
            path.add((i, j))
            return grid[i][j] + cur_max, path

        max_path = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # we try every value which is not 0 and not in the current max_path
                if grid[i][j] != 0 and (i, j) not in max_path:
                    val, p = dfs(i, j)
                    if val > max_val:
                        max_val = val
                        max_path = p
        return max_val