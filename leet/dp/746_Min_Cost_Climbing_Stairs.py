import math
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        memo = {}

        def helper(i):
            if i == n:
                return 0
            if i > n:
                return math.inf
            if i not in memo:
                memo[i] = min(helper(i + 1) + cost[i], helper(i + 2) + cost[i])
            return memo[i]

        first, sec = 0, 0
        for i in range(0, n):
            if i == n - 1:
                third = min(first + cost[i], sec)
            else:
                third = min(first, sec) + cost[i]
            first, sec = sec, third
        return sec


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        if n <= 2:
            return min(cost)

        one = two = 0
        for i in range(2, n + 1):
            two, one = one, min(two + cost[i - 2], one + cost[i - 1])
        return one