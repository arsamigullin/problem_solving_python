#
# assign buy to be max and profit to be 0
# on each element assume you sold at this value
# evaluate max_profit(must be greater than latest val) and next buy(must be less than curr val)
class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return max_profit