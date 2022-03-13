import math
from typing import List

# similar 1014 256 265 931 1289 1937

class Solution:
    def maxPoints(self, A):
        m, n = len(A), len(A[0])
        for i in range(m - 1):
            # we start from the n-2 element and compare it with  the one to the right - 1
            # -1 is to account the problem condition
            # 'However, you will lose points if you pick a cell too far from the cell that you picked in the previous row.
            # For every two adjacent rows r and r + 1 (where 0 <= r < m - 1),
            # picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.'

            # suppose we have initial array
            # 1 3 5 7 -> after running the first internal loop (right to left direction) for the first row  4 5 6 7
            # 2 4 8 1
            for j in range(n - 2, -1, -1):
                A[i][j] = max(A[i][j], A[i][j + 1] - 1)

            for j in range(n):
                # here we do the same but for left to right direction
                A[i][j] = max(A[i][j], A[i][j - 1] - 1 if j else 0)
                # and we add up the max value we got from the current row to the next row
                # the beauty here is when adding A[i][j] to the next row the A[i][j] already accountant for abs(c1 - c2)
                A[i + 1][j] += A[i][j]
        return max(A[-1])

# clean version
class Solution:
    def maxPoints(self, A: List[List[int]]) -> int:

        n = len(A)
        m = len(A[0])

        for i in range(n - 1):

            for j in range(m - 2, -1, -1):
                A[i][j] = max(A[i][j], A[i][j + 1] - 1)
            for j in range(m):
                A[i][j] = max(A[i][j], A[i][j - 1] - 1 if j else 0)
                A[i + 1][j] += A[i][j]
        return max(A[-1])

# wrong
class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        memo = {}
        n = len(points)
        m = len(points[0])

        def helper(i, c):
            if i >= n:
                return 0
            if i not in memo:
                max_val = -math.inf
                for j in range(m):
                    max_val = max(max_val, helper(i + 1, j) + points[i][j] - abs(c - j))
                memo[i] = max_val
            return memo[i]

        ans = -math.inf
        for j in range(m):
            ans = max(helper(0, j), ans)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.maxPoints([[1,2,3],[1,5,1],[3,1,1]])
    s.maxPoints([[1,5],[2,3],[4,2]])

