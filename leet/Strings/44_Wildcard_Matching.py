class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        memo = {}

        def helper(i, j):
            if i >= n:
                return j == m or all(p[i] == '*' for i in range(j, m))
            if j >= m:
                return i == n
            if (i, j) not in memo:
                res = False
                if i < n and s[i] == p[j] or p[j] == '?':
                    res = helper(i + 1, j + 1)
                # with the asterix try three different options
                if p[j] == '*':
                    res = helper(i + 1, j) or helper(i + 1, j + 1) or helper(i, j + 1)
                memo[(i, j)] = res
            return memo[(i, j)]

        return helper(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        i = j = 0
        star_idx = s_tmp_idx = -1

        while i < n:
            # If the pattern caracter = string character
            # or pattern character = '?'
            if j < m and p[j] in ['?', s[i]]:
                i += 1
                j += 1

            # If pattern character = '*'
            elif j < m and p[j] == '*':
                # Check the situation
                # when '*' matches no characters
                star_idx = j
                s_tmp_idx = i
                j += 1

            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern
            elif star_idx == -1:
                return False

            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
            else:
                # Backtrack: check the situation
                # when '*' matches one more character
                j = star_idx + 1
                i = s_tmp_idx + 1
                s_tmp_idx = i

        # The remaining characters in the pattern should all be '*' characters
        return all(p[i] == '*' for i in range(j, m))