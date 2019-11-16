def solution(a,b):
    n = len(a)
    m = len(b)
    dp = [[0] * (n + 1) for _ in range(m+1)]
    max_len = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i-1][j-1]+1
                max_len = max(max_len, dp[i][j])

    return max_len

if __name__ == "__main__":
    print(solution([0,0,0,0,1], [1,0,0,0,0]))
#    1, 0, 0, 0, 0
#0 [[0, 0, 0, 0, 0, 0], if a[i - 1] == b[j - 1], i.e. 0==1
#0 [0, 0, 1, 1, 1, 1], note we start forming dp[1][1]
#0 [0, 0, 1, 2, 2, 2],
#0 [0, 0, 1, 2, 3, 3],
#1 [0, 0, 1, 2, 3, 4],
#  [0, 1, 0, 0, 0, 0]]