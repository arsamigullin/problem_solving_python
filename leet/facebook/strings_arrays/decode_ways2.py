class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)

        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(s) + 1):
            # One step jump
            c = s[i - 1:i]
            if c == '*':
                dp[i] += dp[i - 1]  + 9
            elif 0 < int(s[i - 1:i]):  # (2)
                dp[i] += dp[i - 1]
            # Two step jump
            e = s[i - 2:i]
            if '*' in e:
                cnt = 0
                for j in range(1,10):
                    if 10 <= int(e.replace('*', str(j))) <= 26:
                        cnt+=1
                dp[i] += dp[i - 2] + cnt
            elif 10 <= int(e) <= 26:  # (3)
                dp[i] += dp[i - 2]

        return dp[-1]%(10**9+7)
if __name__ == "__main__":
    s = Solution()
    s.numDecodings("12*")