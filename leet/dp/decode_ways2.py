
class SolutionDoesNotWork:
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


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        M = 10 ** 9 + 7
        memo = [0] * n

        def ways(s, i):
            if i < 0:
                return 1
            if not memo[i]:
                if s[i] == '*':
                    res = 9 * ways(s, i - 1) % M
                    if i > 0 and s[i - 1] == '1':
                        res = (res + 9 * ways(s, i - 2)) % M
                    elif i > 0 and s[i - 1] == '2':
                        res = (res + 6 * ways(s, i - 2)) % M
                    elif i > 0 and s[i - 1] == '*':
                        res = (res + 15 * ways(s, i - 2)) % M
                    memo[i] = res
                else:
                    res = 0 if s[i] == '0' else ways(s, i - 1)
                    if i > 0 and s[i - 1] == '1':
                        res = (res + ways(s, i - 2)) % M
                    elif i > 0 and s[i - 1] == '2' and s[i] <= '6':
                        res = (res + ways(s, i - 2)) % M
                    elif i > 0 and s[i - 1] == '*':
                        res = (res + (2 if s[i] <= '6' else 1) * ways(s, i - 2)) % M
                    memo[i] = res
            return memo[i]

        return ways(s, n - 1)

if __name__ == "__main__":
    s = Solution()
    s.numDecodings("1111")