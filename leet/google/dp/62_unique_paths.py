class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(m):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = dp[j-1][i]+dp[j][i-1]
        return dp[n-1][m-1]
