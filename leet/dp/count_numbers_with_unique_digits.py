def solution(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = dp[i-1] + 10
        elif i == 2:
            dp[i] = dp[i - 1] + 81
        else:
            res = 9 * 9
            j = 2
            cnt = 8
            while j < i:
                res *= cnt
                cnt-=1
                j += 1
            dp[i] = dp[i - 1] + res
    return dp[n]

if __name__ == "__main__":
    print(solution(4))

# condition says 0<=x<10^n
# let's consider n = 4
# the first ten nums are unique so it is 10
# 2 digit number has 9 * 9 total unique numbers. 9 is because number cannot start from 0, so 10 - 1 = 9.
# The second one is 9 because it can have 0 but should not include number from the first number, so  10 - 1 = 9
# the third number should not include number from second number 9 * 9 * 8
# the fourth number should not include number from third number 9 * 9 * 8 * 7
# the total is
# 10 + (10 + 9 * 9 ) + (91 + 9 * 9 * 8) + (739 + 9 * 9 * 8 * 7)
