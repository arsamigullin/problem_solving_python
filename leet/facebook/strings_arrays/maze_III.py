import collections
import typing
List = typing.List
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        d, r, l, u = 'd', 'r', 'l', 'u'
        
        dirs = {d: (1, 0), r: (0, 1), l: (0, -1), u: (-1, 0)}
        a, b = ball
        maze[a][b] = -1
        q = collections.deque()
        for direction in (r, l, d, u):
            rowOffset, colOffset = dirs[direction]
            dx, dy = a + rowOffset, b + colOffset
            if dx < 0 or dx >= len(maze) or dy < 0 or dy >= len(maze[0]) or maze[dx][dy] == 1:
                continue
            q.append((dx, dy, direction, 1, direction))
        shortest_path =''
        min_dist = float('inf')
        while q:
            i, j, curDirection, dist, path = q.popleft()
            is_destination = (i == hole[0] and j == hole[1])
            xOffset, yOffset, curDirName = dirs[curDirection]
            x, y = i + xOffset, j + yOffset
            if is_destination:
                if dist == min_dist:
                    shortest_path = min(shortest_path, path)
                elif dist < min_dist:
                    min_dist = dist
                    shortest_path = path
                continue
            # if there is a wall
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
                maze[i][j] = -1
                for direction in (r, l, d, u):
                    rowOffset, colOffset, dirName = dirs[direction]
                    dx, dy = i + rowOffset, j + colOffset

                    if dx < 0 or dx >= len(maze) or dy < 0 or dy >= len(maze[0]) or maze[dx][dy] == -1 or maze[dx][dy] == 1:
                        continue
                    q.append((dx, dy, direction, dist+1, path + dirName))
            else:
                if maze[x][y] != -1:
                    q.append((x, y, curDirection, dist+1, path))

        return 'impossible' if shortest_path == '' else shortest_path
