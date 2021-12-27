import collections
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

# the complete analogy of knapsack problem
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot = sum(stones)
        halfTot = tot//2
        n = len(stones)
        dp = [[0]*(halfTot+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for w in range(1, halfTot+1):
                if stones[i-1] > w:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = max(dp[i-1][w], stones[i-1] + dp[i-1][w - stones[i-1]])
        return tot - 2*dp[-1][-1]

# The value of the final rock would be a summation of all values with +/- signs. As we are trying to minimize the
# size of the final rock, we need to find a partition of numbers in the array into two subsets, which have the
# least amount of differenc in their summations.
# We can reformulate this as a 0-1 Knapsack, i.e. collecting some rocks, where the weights of the rocks is maximized
# and their total weight does not exceed half of the total weight of the rocks.
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        Max_weight = int(total / 2)

        current = (Max_weight + 1) * [0]

        for v in stones:
            for w in range(Max_weight, -1, -1):
                if w - v >= 0:
                    current[w] = max(v + current[w - v], current[w])

        return total - 2 * current[-1]




# knapsack 0-1 problem:
# given n items, and backpack with capacity W. Each item has its value and weight. We need to choose items to put them
# to the bapckpack so the total their weight is not exceeds the bacpack's capacity and the total value is maximized

# approach 1 (recursion with memoization)




