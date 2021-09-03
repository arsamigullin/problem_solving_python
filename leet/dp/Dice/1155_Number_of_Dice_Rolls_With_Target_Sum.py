class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        M = 10 ** 9 + 7
        memo = {}

        def dfs(i, remain):
            if remain < 0:
                return 0
            if i > d:
                return int(remain == 0)
            if (i, remain) not in memo:
                r = 0
                for j in range(1, f + 1):
                    if remain - j < 0:
                        break
                    r += dfs(i + 1, remain - j) % M
                memo[(i, remain)] = r % M
            return memo[(i, remain)]

        return dfs(1, target)


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target > d * f:
            return 0

        # dp[i][j] -> num of ways to reach target = i with j dices
        dp = [[0 for i in range(d + 1)] for j in range(target + 1)]
        dp[0][0] = 1

        for k in range(1, target + 1):
            for i in range(1, min(d + 1, k + 1)):
                for j in range(1, min(f + 1, k + 1)):
                    dp[k][i] = (dp[k][i] + dp[k - j][i - 1]) % (1e9 + 7)
        return int(dp[target][d] % (1e9 + 7))


from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(d, t):
            # Prune invalid combinations early (~65% reduction in runtime)
            if d * f < t or t < d:
                return 0
                # Determine if this is a valid combination
            if d == 1:
                return 1 <= t <= f
                # Count the number of combinations for each face of the die.
            return sum(dp(d - 1, t - i) for i in range(max(1, t - (d - 1) * f), min(f + 1, t)))

        return dp(d, target) % (10 ** 9 + 7)