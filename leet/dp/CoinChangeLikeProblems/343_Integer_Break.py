class Solution:
    def integerBreak(self, n: int) -> int:

        memo = {}
        def helper(remain, k):
            if remain == 0 and k >= 2:
                return 1
            if remain not in memo:
                res = 0
                for i in range(1, remain + 1):
                    if i <= remain:
                        res = max(res, helper(remain - i, k + 1) * i)
                memo[remain] = res
            return memo[remain]

        return helper(n, 0)


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], dp[i - j] * j, j * (i - j))

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.integerBreak(4)