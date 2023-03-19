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

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m+1) for _ in range(n+1)]
        print(dp)

        for i in range(n):
            for j in range(m):
                if j == 0:
                    dp[i+1][j+1] = min(dp[i][j+1], 0 if j+2>=m+1 else dp[i][j+2]) + matrix[i][j]
                elif j == m - 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1]) + matrix[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], 0 if j+2>=m+1 else dp[i][j+2]) + matrix[i][j]
        return min(dp[-1][1:])
