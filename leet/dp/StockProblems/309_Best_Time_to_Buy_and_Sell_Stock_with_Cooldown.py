from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def helper(i, state, buy):
            if i >= n:
                return 0
            if (i, state) not in memo:
                if state == 'cooldown':
                    memo[(i, state)] = helper(i + 1, 'buy', prices[i])
                elif state == 'hold':
                    memo[(i, state)] = max(helper(i + 1, 'sell', 0) + (prices[i] - buy), helper(i + 1, 'hold', buy),
                                           helper(i + 1, 'buy', prices[i]))
                elif state == 'buy':
                    memo[(i, state)] = max(helper(i + 1, 'sell', 0) + (prices[i] - buy), helper(i + 1, 'hold', buy),
                                           helper(i + 1, 'buy', prices[i]))
                elif state == 'sell':
                    memo[(i, state)] = helper(i + 1, 'cooldown', 0)
            return memo[(i, state)]

        return helper(1, 'buy', prices[0])

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        buy = [-prices[0]]
        cool, sell = 0, 0
        for price in prices[1:]:
            buy.append(cool - price)
            cool = max(cool, sell)
            sell = price + max(buy[:-1])
        return max(sell, cool)


if __name__ == '__main__':
    s = Solution()
    s.maxProfit([6,1,3,2,4,7])