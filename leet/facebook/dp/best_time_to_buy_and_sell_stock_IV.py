import collections
class Solution1:
    def maxProfit(self, prices: list) -> int:
        m = float('inf')
        dp = [0] * (len(prices)+1)
        dp1 = [0] * (len(prices)+1)
        for i in range(len(prices)):
            dp[i + 1] = prices[i] - m
            m = min(m, prices[i])

        m = float('-inf')
        for i in range(len(prices) - 1, -1 ,-1):
            dp1[i] = m - prices[i]
            m = max(m, prices[i])
        print(dp)
        print(dp1)
        m = 0
        for a,b in zip(dp, dp1):
            m = max(m, a + b)
        return m

class Solution:
    def maxProfit(self, prices: list) -> int:

        if not prices:
            return 0
        b1 = b2 = -prices[0]
        s1 = s2 = 0
        for i in prices:
            s1 = max(s1, b1+i)
            b1 = max(b1, -i)
            s2 = max(s2, b2+i)
            b2 = max(b2, s1-i)
        return s2


if __name__ == "__main__":
    s = Solution()
    s.maxProfit([1,2,4,2,5,7,2,4,9,0])
