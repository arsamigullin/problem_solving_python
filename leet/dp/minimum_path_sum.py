def solution(grid):
    m= len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i - 1]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
    return dp[m-1][n-1]
if __name__ == "__main__":
    solution([[1,3,1],[1,5,1],[4,2,1]])