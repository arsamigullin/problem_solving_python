import math
from typing import List


def solution(amount,coins):
    d = [amount + 1] * (amount + 1)
    d[0] = 0
    for m in range(1, amount + 1):
        for j in range(len(coins)):
            c = coins[j]
            if c <= m:
                d[m] = min(d[m], d[m - c] + 1)
    print(d)
    return -1 if d[amount] > amount else d[amount]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def helper2(am):
            if am == 0:
                return 0
            if am < 0:
                return -1
            if am not in memo:
                min_cost = math.inf
                for c in coins:
                    res = helper2(am - c)
                    if res != -1:
                        min_cost = min(min_cost, res + 1)
                memo[am] = -1 if min_cost == math.inf else min_cost
            return memo[am]

        return helper2(amount)

if __name__ == "__main__":
    print(solution(8,[1,3]))
    #print(solution(9,[1,3]))
    #print(solution(6, [1, 2, 3]))
    #print(solution(11,[1,2,5]))
