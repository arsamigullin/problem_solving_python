def solution(s):
    d = dict()

    def find(i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return find(i + 1, j - 1) + 2
        key = str(i) + "|" + str(j)
        # print(key)
        if key not in d:
            d[key] = max(find(i + 1, j), find(i, j - 1))
        return d[key]

    find(0, len(s) - 1)
    print(d)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        memo = {}

        def helper(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) not in memo:
                if s[l] == s[r]:
                    cnt = helper(l + 1, r - 1) + 2
                else:
                    cnt = max(helper(l + 1, r), helper(l, r - 1))
                memo[(l, r)] = cnt
            return memo[(l, r)]

        return helper(0, n - 1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # this is start loop
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            # this is end loop
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]


if __name__ == "__main__":
    print(solution("abcdeca"))
    # print(solution("fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd"))
