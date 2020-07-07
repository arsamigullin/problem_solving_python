from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        tot = sum(stones)

        dp = [0 for i in range(tot // 2 + 1)]
        dp[0] = 1

        for stone in stones:
            for i in range(tot // 2, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]

        for i in range(len(dp) - 1, -1, -1):
            if dp[i] > 0:
                return tot - 2 * i