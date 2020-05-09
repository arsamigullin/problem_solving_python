from typing import List

# similar
# # 256, 265, 931, 1289
# O(M*N)
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        N = len(A)
        M = len(A[0])
        for i in range(1, N):
            for j in range(M):
                _min = float('inf')
                # this is O(1)
                for di, dj in ([-1, 0], [-1, -1], [-1, 1]):
                    x, y = i + di, j + dj
                    if 0 <= x < N and 0 <= y < M:
                        _min = min(_min, A[x][y])
                A[i][j] += _min

        return min(A[-1])