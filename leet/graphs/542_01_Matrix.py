import collections
import math
from typing import List

# this is BFS
# Quite regular algo
# collect zeros and then do BFS updating mat
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        n = len(mat)
        m = len(mat[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            i, j, dist = q.popleft()
            mat[i][j] = dist
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                    q.append((x, y, dist + 1))
                    visited.add((x, y))
        return mat

# iterage from top left corner then iterate from bottom right cornerLast Stone Weight
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    min_dist = math.inf
                    for x, y in [(i - 1, j), (i, j - 1)]:
                        if 0 <= x < n and 0 <= y < m:
                            min_dist = min(min_dist, dp[x][y])
                    dp[i][j] = min_dist + 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 1:
                    min_dist = math.inf
                    for x, y in [(i + 1, j), (i, j + 1)]:
                        if 0 <= x < n and 0 <= y < m:
                            min_dist = min(min_dist, dp[x][y])
                    dp[i][j] = min(dp[i][j], min_dist + 1)
        return dp