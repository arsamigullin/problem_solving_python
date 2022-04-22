import collections
from typing import List

# two approaches

# collect a source point (which is guaranteed to be only one there)
class Solution1:
    def getFood(self, grid: List[List[str]]) -> int:

        q = collections.deque()
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    q.append((i, j, 0))
                    grid[i][j] = 'X'

        while q:
            x, y, dist = q.popleft()
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < n and 0 <= j < m:
                    if grid[i][j] == '#':
                        return dist + 1
                    if grid[i][j] == 'O':
                        grid[i][j] = 'X'
                        q.append((i, j, dist + 1))
        return -1

# collect all target points (there may be multiple of them)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:

        q = collections.deque()
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    q.append((i, j, 0))
                    grid[i][j] = 'X'

        while q:
            x, y, dist = q.popleft()
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < n and 0 <= j < m:
                    if grid[i][j] == '*':
                        return dist + 1
                    if grid[i][j] == 'O':
                        grid[i][j] = 'X'
                        q.append((i, j, dist + 1))
        return -1

