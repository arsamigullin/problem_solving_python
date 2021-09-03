import math
from typing import List


class Solution(object):
    def minimumMoves(self, A):
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i,j) not in memo:
                res = dp(i, j - 1) + 1
                if A[j] == A[j - 1]:
                    # removing two adjacent similar nums costs 1
                    # doing dp(i, j - 2) we check how much removals need in arr[i:j-2]
                    res = min(res, dp(i, j - 2) + 1)
                for k in range(i, j - 1):
                    # still not clear why this check is important
                    # the best guess is if they are equal that could be a palindrome which can decrease the min value
                    if A[k] == A[j]:
                        # why don't we add 1 to dp(k + 1, j - 1)
                        # because A[k] = A[j] and whatever removals it returns one of them reserved to remove arr[i:j]
                        # for example arr=1,3,4,1 and their indices is 0,1,2,3
                        # so arr[k] = arr[j], dp(k + 1, j - 1) returns 2 removals (need to remove 4 and 3).
                        # but after removing 3, 1,4,1 palindrome left which takes only one removal
                        res = min(res, dp(i, k - 1) + dp(k + 1, j - 1))
                memo[(i,j)] = res
            return memo[(i,j)]
        return dp(0, len(A) - 1)

# this very similar to 647_Palindromic_Substrings.py
class Solution1:
    def minimumMoves(self, arr: List[int]) -> int:

        n = len(arr)
        dp = [[math.inf] * n for _ in range(n)]
        # it take one step to remove one item
        for i in range(n):
            dp[i][i] = 1
        # it takes 1 step to remove 2 the same adjacent items
        # or if they are different, it takes 2 steps
        for i in range(n - 1):
            dp[i][i + 1] = 1 if arr[i] == arr[i + 1] else 2

        # length 1 and 2 were worked out
        # now need to explore all palindromes with len 3 and more
        for lenght in range(3, n + 1):
            i = 0
            j = i + lenght - 1
            while j < n:
                # if arr[i] ane arr[j] are the same, it takes the same removals that required the inner substring
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    # we take mid and explore different substrings
                    for mid in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                j += 1
                i += 1

        return dp[0][n - 1]


if __name__ == '__main__':
    s = Solution()
    s.minimumMoves([1,2,1, 14, 18, 20, 14])
    s.minimumMoves([1, 14, 18, 20, 14]) # this proves that this part is required dp(i, k - 1)
    s.minimumMoves([1, 3, 4, 1, 5])
    s.minimumMoves([1,2,2,1])

    s.minimumMoves([1, 1])
    s.minimumMoves([16,13,13,10,12]) #this proves that this check required if A[j] == A[j - 1]: