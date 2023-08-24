class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)
        memo = {}

        def helper(i, j):
            if i == n or j == m:
                return 0
            if (i, j) not in memo:
                if s[i] == t[j]:
                    memo[(i, j)] = helper(i + 1, j + 1) + 1
                else:
                    memo[(i, j)] = max(helper(i + 1, j), helper(i, j + 1))
            return memo[(i, j)]

        return helper(0, 0)

# s = ace
# t = abcde
#
#   a b c d e @
# a 3 2 2 1 1 0
# c 2 2 2 1 1 0
# e 1 1 1 1 1 0
# @ 0 0 0 0 0 0
#
#
#



class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]