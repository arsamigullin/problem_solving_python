# this is O(1) https://leetcode.com/problems/integer-break/discuss/423970/O(1)-Solution

# this is O(n)
def solution(n):
    i = 2
    dp = [1] * (n+1)
    dp[1] = 1
    while i<=n:
        d = 1
        while i - d > 0:
            dp[i] = max(dp[i], dp[d] * dp[i-d])
            # if i is not a given number we also must cover the the i * 1 case (i.e. i)
            if i != n:
                dp[i] = max(dp[i], i)
            d+=1
        i+=1
    return dp[n]

if __name__ == "__main__":
    print(solution(10))