import collections
import typing
List = typing.List

# Algo
# at the beginning we figure out the allowed directions and append direction and node coordinates to the queue
# then we iterate over queue using BFS
# when popping the node we check if there is a wall on direction of this current node
# only when we found a wall we mark this position as visited since 
# we mark it as visited (-1) since if we got here the second time we would 
# go the same path. To reduce it we mark it as visited (-1)

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        DOWN, RIGHT, LEFT, UP = 0, 1, 2, 3
        d = {DOWN: (1, 0), RIGHT: (0, 1), LEFT: (0, -1), UP: (-1, 0)}
        a, b = start
        maze[a][b] = -1
        q = collections.deque()

        # this help us check if we reached the destination
        # since this function is called only when the wall was found 
        # we 100% that the ball will stop
        def gotDestination(i, j, curDirection):
            for direction in (RIGHT, LEFT, DOWN, UP):
                is_destination = (i == destination[0] and j == destination[1])
                dx, dy = i + d[direction][0], j + d[direction][1]
                if is_destination and direction == curDirection:
                    return True
                if dx < 0 or dx >= len(maze) or dy < 0 or dy >= len(maze[0]) or maze[dx][dy] == -1 or maze[dx][dy] == 1:
                    continue
                q.append((dx, dy, direction))
            return False

        gotDestination(a,b,-1)

        while q:
            i, j, curDirection = q.popleft()
            x, y = i + d[curDirection][0], j + d[curDirection][1]
            # if there is a wall on direction of the current node
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
                # only when we found a wall we mark this position as visited since 
                # we mark it as visited (-1) since if we got here the second time we would 
                # go the same path. To reduce it we mark it as visited (-1)
                maze[i][j] = -1

                if gotDestination(i,j,curDirection):
                    return True
            elif maze[x][y] != -1:
                q.append((x, y, curDirection))

        return False
if __name__ == "__main__":
    s = Solution()
    s.hasPath([ [0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1],
                [0,1,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,1,0,0,0,1],
                [0,0,0,0,1,0,0]],
                [0,0],[8,6])
    #s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[1,2])
    #s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4])
    #s.hasPath([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]],[4,3],[0,1])
    #s.hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4],[3,2])