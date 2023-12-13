from typing import List


class Solution1:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit+= prices[i] - prices[i-1]
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def helper(i, buy):
            if i >= n:
                return 0
            if i not in memo:
                # for testing purposes
                # we sell the stock (prices[i]-buy) and trying to buy it on the same price (helper(i + 1, prices[i])))
                first = prices[i] - buy + helper(i + 1, prices[i])
                # we are getting minimum buy price and trying to sell it
                sec = helper(i + 1, min(buy, prices[i]))
                print(first, sec)
                memo[i] = max(first, sec)
                # all above we write as this
                # memo[i] = max(prices[i] - buy + helper(i + 1, prices[i]), helper(i + 1, min(buy, prices[i])))
            return memo[i]

        return helper(0, 10 ** 6)

if __name__ == '__main__':
    s = Solution2()
    s.maxProfit([7,1,5,3,6,4])