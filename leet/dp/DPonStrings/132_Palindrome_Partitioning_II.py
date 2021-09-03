class Solution:
    def minCut(self, s: str) -> int:

        memo = {}
        memoPalindrome = {}

        def findMinCut(s, i, j, minCut):
            if i == j or isPalindrome(s, i, j):
                return 0
            if (i, j) not in memo:
                for k in range(i, j + 1):
                    if isPalindrome(s, i, k):
                        minCut = min(minCut, findMinCut(s, k + 1, j, minCut) + 1)
                memo[(i, j)] = minCut
            return memo[(i, j)]

        def isPalindrome(s, i, j):
            if i >= j:
                return True
            if (i, j) not in memoPalindrome:
                memoPalindrome[(i, j)] = s[i] == s[j] and isPalindrome(s, i + 1, j - 1)
            return memoPalindrome[(i, j)]

        return findMinCut(s, 0, len(s) - 1, len(s) - 1)