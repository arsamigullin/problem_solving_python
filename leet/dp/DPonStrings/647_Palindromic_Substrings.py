class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False] * n for _ in range(n)]
        # single letter is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans += 1
        # count the palindroms consisting of two chars
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            ans += int(dp[i][i + 1])

        # if aba is palindrome, then xabax is also palindrome
        # aba is already been evaluated, so when evaluating xabax we just
        # compare s[0] with s[-1]
        for l in range(3, n + 1):
            i = 0
            j = i + l - 1
            while j < n:
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                ans += int(dp[i][j])
                i += 1
                j += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    s.countSubstrings("xabax")