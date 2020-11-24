from typing import List


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1: [1]}

        def helper(n):
            if n not in memo:
                odds = helper((n + 1) // 2)
                evens = helper(n // 2)
                res = [2 * x - 1 for x in odds] + [2 * x for x in evens]
                memo[n] = res
            return memo[n]

        return helper(N)