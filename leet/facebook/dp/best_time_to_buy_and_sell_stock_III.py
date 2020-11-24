
# the idea here is to do front traversal and back traversal
# doing front traversal we are tracking max profit at first transaction
# by considering only smallest smallest price (since first we buy, buy price comes first)
# doing back traversal we are tracking max profit at second transaction
# by considering the biggest sell price (since we sell secondly, sell price comes first when going back)|
# or think it that way:
# once we bought we do not have the minimum price anymore, therefore we cannot use the minimum we found when front
# traversing
# the back traverse comes into play. It allows considering new mininmum
import collections
class Solution1:
    def maxProfit(self, prices: list) -> int:
        m = float('inf')
        dp = [0] * (len(prices)+1)
        dp1 = [0] * (len(prices)+1)
        for i in range(len(prices)):
            dp[i + 1] = max(prices[i] - m, dp[i])
            m = min(m, prices[i])

        m = float('-inf')
        for i in range(len(prices) - 1, -1 ,-1):
            dp1[i] = max(m - prices[i], dp1[i + 1])
            m = max(m, prices[i])
        m = 0
        for a,b in zip(dp, dp1):
            m = max(m, a + b)
        return m

# this solution will not work because
# it does not track the position of the max profit when going forward and backward
import collections
class Solution2:
    def maxProfit(self, prices: list) -> int:
        b = prices[0]
        profit = 0
        for i in range(len(prices)):
            profit = max(prices[i] - b, profit)
            b = min(b, prices[i])


        s = prices[-1]
        pr = 0
        for i in range(len(prices) - 1, -1 ,-1):
            pr = max(s - prices[i], pr)
            s = max(s, prices[i])

        return profit + pr

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
    s = Solution1()
    s.maxProfit([3,3,5,0,0,3,1,4])

    #print(s.maxProfit([5,2,3,0,3,5,6,8,1,5]))