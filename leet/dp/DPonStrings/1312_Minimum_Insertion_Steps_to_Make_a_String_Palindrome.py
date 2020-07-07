# we need to find minimum insertions to make the string s palindrome

class SolutionMy:
    def minInsertions(self, s: str) -> int:
        d = {}

        def dfs(i, j):
            # the length of s is even
            # no insertion needed
            if i > j:
                return 0
            # the length of s is odd
            # again, no insertions needed
            if i == j:
                return 0
            # if chars are equal we move left and right pointers
            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            # if we here that means the chars under left and right pointers are not equal
            # now if we do not have in d insertions count for the substring between i and j
            # we calculate it
            if (i, j) not in d:
                d[(i, j)] = min(dfs(i + 1, j), dfs(i, j - 1)) + 1
            return d[(i, j)]

        res = dfs(0, len(s) - 1)
        return res


# iterative solution

class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        return len(s) - self.lenLongestPalindromicSubSequence(s)

    def lenLongestPalindromicSubSequence(self, s):
        n = len(s)
        lps = [[0] * n for _ in range(n)]
        # fill diagonal with ones

        for i in range(n):
            lps[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lps[i][j] = 2 + lps[i + 1][j - 1]
                else:
                    lps[i][j] = max(lps[i + 1][j], lps[i][j - 1])
        return lps[0][-1]


if __name__ == '__main__':
    s = Solution()
    s.minInsertions("ab")
