import collections


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word2) + 1)

        for i, l in enumerate(word1):
            new_dp = [0] * (len(word2) + 1)
            for j, k in enumerate(word2):
                new_dp[j + 1] = dp[j] + 1 if l == k else max(dp[j + 1], new_dp[j])

            dp = new_dp

        return len(word1) + len(word2) - 2 * dp[-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    dp[i][j] = i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j])
        return dp[-1][-1]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = collections.defaultdict(int)

        def helper(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if (i, j) not in dp:
                if word1[i] == word2[j]:
                    dp[(i, j)] = helper(i + 1, j + 1)
                else:
                    dp[(i, j)] = min(helper(i + 1, j), helper(i, j + 1)) + 1
            return dp[(i, j)]

        res = helper(0, 0)
        return res