from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def is_palindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        memo = {}

        def helper(i, pal):
            if i >= n:
                res.append(pal[:])
                return
            for j in range(i, n):
                if (i, j) not in memo:
                    memo[(i, j)] = is_palindrome(i, j)
                if memo[(i, j)]:
                    pal.append(s[i:j + 1])
                    helper(j + 1, pal)
                    pal.pop()

        helper(0, [])
        return res

