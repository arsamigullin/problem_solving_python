from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        n = len(maze)
        m = len(maze[0])

        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            i, j, dist = q.popleft()
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x = i + dx
                y = j + dy
                if (x >= n or x < 0 or y >= m or y < 0) and (i != entrance[0] or j != entrance[1]):
                    return dist
                if 0 <= x < n and 0 <= y < m and maze[x][y] == '.':
                    maze[x][y] = '+'
                    q.append((x, y, dist + 1))

        return -1