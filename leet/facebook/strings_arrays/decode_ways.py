class Solution:
    def numDecodings(self, s):
        v = 0
        w = int(s > '')
        p = ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w

#w tells the number of ways
#v tells the previous number of ways
#d is the current digit
#p is the previous digit

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
if __name__ == "__main__":
    s= SolutionDp()
    s.numDecodings("199")