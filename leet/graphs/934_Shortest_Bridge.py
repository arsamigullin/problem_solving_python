import collections
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        cmp = collections.defaultdict(int)

        n = len(grid)
        m = len(grid[0])
        num = 0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in cmp:
                    num += 1
                    q = deque([(i, j)])
                    cmp[(i, j)] = num
                    while q:
                        x, y = q.popleft()
                        if num == 1:
                            queue.append((x, y, 0))
                        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                            nx = dx + x
                            ny = dy + y
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and (nx, ny) not in cmp:
                                q.append((nx, ny))
                                cmp[(nx, ny)] = num

        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1 and cmp[(nx, ny)] == 2:
                        return dist
                    elif grid[nx][ny] == 0:
                        queue.append((nx, ny, dist + 1))
                        grid[nx][ny] = -1
        return -1


