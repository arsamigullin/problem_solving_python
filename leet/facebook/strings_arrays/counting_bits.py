# both solutions are the same
# dp contains nums of bits that for particular number represented by index
# for example dp[1] - contains count of bits of number 1 and so on
# Algo
# if the number is odd then the count of bits of that odd number equals count of bits of number number//2 + 1
# otherwise it just equals the number of bits of number number//2
class Solution:
    def countBits(self, num: int) -> list:
        dp = [0] * (num + 1)
        for x in range(1, num + 1):
            if x & 1:
                dp[x] = dp[x >> 1] + 1
            else:
                dp[x] = dp[x >> 1]
        return dp

class Solution:
    def countBits(self, num: int) -> list:
        dp = [0] * (num + 1)
        for x in range(1, num + 1):
            if x%2 == 1:
                dp[x] = dp[x//2] + 1
            else:
                dp[x] = dp[x//2]
        return dp

if __name__ == "__main__":
    s = Solution()
    s.countBits(5)