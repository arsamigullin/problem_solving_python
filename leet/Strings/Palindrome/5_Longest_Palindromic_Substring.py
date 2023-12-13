class Solution:
    def longestPalindrome(self, s: str) -> str:

        def get_palindrome(s, lo, hi):
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return s[lo + 1:hi]

        # there are 2*n-1 possible midpoints in palindrome
        n = len(s)
        larget_palindrome = ""
        for i in range(n):
            # case 1: aba, both lo and hi point to the middle
            candidate = get_palindrome(s, i, i)
            if len(larget_palindrome) < len(candidate):
                larget_palindrome = candidate
            # case 2: abba, lo points to the first b, hi points to the second b
            candidate = get_palindrome(s, i, i + 1)
            if len(larget_palindrome) < len(candidate):
                larget_palindrome = candidate
        return larget_palindrome


class Solution:
    def longestPalindrome(self, s: str) -> str:

        lo = hi = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
            lo = i
            hi = i + 1

        # palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                lo = i
                hi = i + 2

        # palindromes of length 3 and more
        # the dp array has vaules only above the main diagonal because in the dp array
        # row represents start of the palindrome substring
        # col represents end of the palindrome substring
        # and since start cannot be less than end, when we increase start (row)
        # the end(col) must be the same or greater than start (row)
        for k in range(2, n):
            i = 0
            j = k
            while j < n:
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    lo = i
                    hi = j + 1
                i += 1
                j += 1

        return s[lo: hi]