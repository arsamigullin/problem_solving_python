from collections import deque
from typing import List

#BFS O(m*n*max(n*m))
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        n = len(maze)
        m = len(maze[0])
        seen = set()
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        q = deque()
        for direction in [UP, DOWN, LEFT, RIGHT]:
            q.append((start[0], start[1], 0, direction))

        def canstop(x, y):
            return x < 0 or x >= n or y < 0 or y >= m or maze[x][y] == 1

        while q:
            i, j, distance, direction = q.popleft()
            if (i, j) in seen:
                continue
            x = i + direction[0]
            y = j + direction[1]
            if canstop(x, y):
                if i == destination[0] and j == destination[1]:
                    return distance
                else:
                    seen.add((i, j))
                    for dx, dy in [UP, DOWN, LEFT, RIGHT]:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and (x, y) not in seen:
                            q.append((x, y, distance + 1, (dx, dy)))
            else:
                q.append((x, y, distance + 1, direction))

        return -1







if __name__ == '__main__':
    s = Solution()
    s.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4])