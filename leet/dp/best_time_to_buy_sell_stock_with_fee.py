from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # let's say we had 0 and bought prices[0]
        # so we left with negative amount
        left_after_buy = -prices[0]
        # we did not sell yet
        left_after_sell = 0

        for i in range(len(prices)):
            # sell stock
            # we take the max between what we had before sell and the actual selling
            left_after_sell = max(left_after_sell, left_after_buy + prices[i] - fee)
            # buy stock
            # we take the max  between what we had before buying and the actual buying
            left_after_buy = max(left_after_buy, left_after_sell - prices[i])
        return left_after_sell



if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))