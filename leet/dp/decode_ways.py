
# this is DP solution
# we need to find decode ways of chars from A to Z (1-26)
# each  char can be represented at most with two numbers (for example Z is '26')
# we start from 2 and look back on 1 and 2 chars
# when looking back on 1 char we check if it is > 0
# when looking back on chars we check if the number is >10 and <26 to avoid '07'


# Note: dp is initialized with len(s)+1 length
# this gives us the possibility to handle the very latest element of an array

class SolutionDp:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i - 1:i]):  # (2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i - 2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]

# This is actually the same but with O(1) space complexity
#w tells the number of ways
#v tells the previous number of ways
#d is the current digit
#p is the previous digit
class Solution:
    def numDecodings(self, s):
        v = 0
        w = int(s > '')
        p = ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


if __name__ == "__main__":
    s= SolutionDp()
    s.numDecodings("199")