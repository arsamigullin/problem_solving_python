import collections
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        n = len(grid)
        m = len(grid[0])
        min_val = -1
        lands = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    lands.append((i, j, 0))
        mem = [[101] * m for _ in range(n)]
        q = collections.deque(lands)
        visited = set()
        while q:
            i, j, dist = q.popleft()
            if grid[i][j] == 0:
                mem[i][j] = min(mem[i][j], dist)
                min_val = max(min_val, mem[i][j])
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 0 and (x, y) not in visited:
                    q.append((x, y, dist + 1))


        print(mem)
        return min_val


if __name__ == '__main__':
    s = Solution()
    s.maxDistance([[1,0,0,0],
                   [0,0,0,1],
                   [0,0,0,0]])
    s.maxDistance([[1, 0, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]])
