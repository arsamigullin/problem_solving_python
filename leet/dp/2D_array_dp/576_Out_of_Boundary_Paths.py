class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 1000000007
        memo = {}

        def helper(m, n, N, i, j, memo):
            if i == m or n == j or i < 0 or j < 0:
                return 1
            if N == 0:
                return 0
            if (i, j, N) not in memo:
                memo[(i, j, N)] = (helper(m, n, N - 1, i - 1, j, memo) % M +
                                   helper(m, n, N - 1, i + 1, j, memo) % M +
                                   helper(m, n, N - 1, i, j - 1, memo) % M +
                                   helper(m, n, N - 1, i, j + 1, memo) % M) % M

            return memo[(i, j, N)]

        return helper(m, n, maxMove, startRow, startColumn, memo)
