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