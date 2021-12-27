class Solution:
    def countSubstrings(self, s: str) -> int:

        def get_palindrome(s, lo, hi):
            ans = 0
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                lo -= 1
                hi += 1
                ans += 1
            return ans

        # there are 2*n-1 possible midpoints in palindrome
        n = len(s)
        count = 0
        for i in range(n):
            # case 1: aba, both lo and hi point to the middle
            count += get_palindrome(s, i, i)
            # case 2: abba, lo points to the first b, hi points to the second b
            count += get_palindrome(s, i, i + 1)

        return count

