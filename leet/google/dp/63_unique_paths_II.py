from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])
        valToAssign = obstacleGrid[0][0]
        for i in range(1, N):
            # once we've met an obstacle the rest of the values are 0
            if obstacleGrid[i][0] == 1:
                valToAssign = 0
            obstacleGrid[i][0] = valToAssign
        valToAssign = 1
        for j in range(1,M):
            # once we've met an obstacle the rest of the values are 0
            if obstacleGrid[0][j] == 1:
                valToAssign = 0
            obstacleGrid[0][j] = valToAssign
        for i in range(1, N):
            for j in range(1, M):
                # once we've met an obstacle
                # we reset it to have no impact from it
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                    obstacleGrid[i][j]+=obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

# even better
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        n = len(g)
        m = len(g[0])

        if g[0][0] == 1:
            return 0

        val = 1
        for i in range(n):
            # once we've met obstacle we can reset the rest of the cells because there will no way
            # to get to the cell after obstacle.
            # even if we meet one more obstacle, we just reset it
            if g[i][0] == 1:
                val = 0
            g[i][0] = val

        val = 1
        for i in range(1, m):
            if g[0][i] == 1:
                val = 0
            g[0][i] = val

        for i in range(1, n):
            for j in range(1, m):
                # reset obstacle to have no impact from it
                if g[i][j] == 1:
                    g[i][j] = 0
                else:
                    g[i][j] = g[i - 1][j] + g[i][j - 1]
        print(g)

        return g[-1][-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        n = len(g)
        m = len(g[0])

        if g[0][0] == 1:
            return 0

        for i in range(n):
            for j in range(m):
                if g[i][j] == 1:
                    g[i][j] = -1

        for i in range(n):
            if g[i][0] == -1:
                break
            else:
                g[i][0] = 1

        for i in range(1, m):
            if g[0][i] == -1:
                break
            else:
                g[0][i] = 1

        for i in range(1, n):
            for j in range(1, m):
                if g[i][j] == -1:
                    continue
                else:
                    g[i][j] = max(g[i - 1][j], 0) + max(g[i][j - 1], 0)
        return 0 if g[-1][-1] == -1 else g[-1][-1]