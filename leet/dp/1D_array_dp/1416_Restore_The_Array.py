class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        start = 0
        i = 0
        mod = 10 ** 9 + 7
        dp[0] = 1
        while i < n:
            if s[i] != '0':
                j = i + 1
                while j <= n and int(s[i:j]) <= k:
                    print(int(s[i:j]))
                    dp[j] += dp[i]
                    dp[j] %= mod
                    j += 1
            i += 1

        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    s.numberOfArrays("1317", 2000)
    s.numberOfArrays("13175", 2000)
    s.numberOfArrays("132", 100)