import collections
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        DOWN, RIGHT, LEFT, UP = 0, 1, 2, 3
        
        d = {DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1), UP: (-1, 0)}
        a, b = start
        maze[a][b] = -1
        q = collections.deque()
        for direction in (RIGHT, LEFT, DOWN, UP):
            rowOffset, colOffset = d[direction]
            dx, dy = a + rowOffset, b + colOffset
            if dx < 0 or dx >= len(maze) or dy < 0 or dy >= len(maze[0]) or maze[dx][dy] == 1:
                continue
            q.append((dx, dy, direction, 1))

        while q:
            i, j, curDirection, dist = q.popleft()
            is_destination = (i == destination[0] and j == destination[1])
            xOffset, yOffset = d[curDirection]
            x, y = i + xOffset, j + yOffset

            # if there is a wall
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
                maze[i][j] = -1
                for direction in (RIGHT, LEFT, DOWN, UP):
                    rowOffset, colOffset = d[direction]
                    dx, dy = i + rowOffset, j + colOffset
                    if is_destination and direction == curDirection:
                        return dist
                    if dx < 0 or dx >= len(maze) or dy < 0 or dy >= len(maze[0]) or maze[dx][dy] == -1 or maze[dx][dy] == 1:
                        continue
                    q.append((dx, dy, direction, dist + 1))
            else:
                if maze[x][y] != -1:
                    q.append((x, y, curDirection, dist + 1))

        return -1