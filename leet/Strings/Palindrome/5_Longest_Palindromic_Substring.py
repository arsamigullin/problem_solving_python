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



