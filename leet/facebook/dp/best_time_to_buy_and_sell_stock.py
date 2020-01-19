class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return max_profit