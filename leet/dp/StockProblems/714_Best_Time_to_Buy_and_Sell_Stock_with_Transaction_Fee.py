import math
from typing import List

# note as many transactions as we want
class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        balance = 0
        balance_left_after_buy = -prices[0]
        for i in range(1, len(prices)):
            # reflects sell, we want to maximize by choosing the highest prices to sell
            balance = max(balance, balance_left_after_buy + prices[i] - fee)
            # reflects buy, we want it to maximize by choosing min price to buy
            balance_left_after_buy = max(balance_left_after_buy, balance - prices[i])
        return balance

# problem 121, but here only one transaction
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = math.inf
        profit = -math.inf
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p - buy)
        return profit


# balance
# buy price
# sell price

if __name__ == '__main__':
    s = Solution1()
    s.maxProfit([6,1,7],2)
    s.maxProfit([1,3,2,8,4,9], 2)