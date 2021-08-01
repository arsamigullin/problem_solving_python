import collections
from typing import List


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
