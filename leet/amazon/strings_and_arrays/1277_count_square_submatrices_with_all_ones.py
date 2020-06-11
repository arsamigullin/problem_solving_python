from _ast import List

# similar
# 221
# dynamic programming

# find explanation in 221

# the difference between 1277

class Solution:
    '''
    in dp at dp[i][j] we store the square side the bottom right corner of which at matrix[i-1][j-1]
    besides dp[i][j] is the side length it is also count of the squares the bottom right corner of which at matrix[i-1][j-1]
    '''
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        tot = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    tot+=dp[i][j]
        return tot