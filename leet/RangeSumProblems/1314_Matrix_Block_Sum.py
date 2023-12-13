# first solve 304
from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        # this is well-known formula for 2D pref sum. It is also encountered in 304
        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + mat[i][j]

        for i in range(n):
            for j in range(m):
                # top left corner (as if in 304)
                c1, r1 = max(0, j - k), max(0, i - k)
                # bottom right corner (as if in 304)
                c2, r2 = min(m - 1, j + k), min(n - 1, i + k)
                # this is well known formula from 304
                mat[i][j] = pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]

        return mat
