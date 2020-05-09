
def solution(m,n):
    # this is wrong initialization of two dimension array:
    # dp = [[0]*m]*n
    #because dp[0][2]=3
    # [[0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3]]
    dp = [[0] * m for _ in range(n)] # this is correct one
    for i in range(n):
        dp[i][0] = 1
    for i in range(m):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j][i] = dp[j-1][i]+dp[j][i-1]
    return dp[n-1][m-1]


if __name__ == "__main__":
    print(solution(7,3))