import bisect

## Cumulative sum less than k, for the input array
## [2,5], 10 -> 7
## [1,3,5,7], 10 -> 9
from typing import List


def csum_less_than_k(nums, k):
    ans = float('-inf')
    slist = [0]

    for x in range(1, len(nums)):
        nums[x] += nums[x-1]

    for p in nums:
        idx = bisect.bisect_left(slist, p-k)
        if idx < len(slist):
            ans = max(ans, p-slist[idx])

        bisect.insort(slist, p)

    return ans

class Solution:
    def maxSumSubmatrix(self, A, k: int) -> int:
        R = len(A)
        C = len(A[0])
        ans = float('-inf')

        ## prefix sum of all A rows
        for r in range(R):
            for c in range(1, C):
                A[r][c] += A[r][c-1]

        ## --|------|---
        ## --|------|---
        ## --|------|---
        ##   l      r
        ## loop through all the cols and inside the window l, r take cumulative sum for each row.
        ## inside the cumulative sum 1d array between l and r, search for the sum less than k

        for l in range(C):
            for r in range(l, C):
                one_d_array = []
                for row in range(R):
                    if l > 0:
                        one_d_array.append(A[row][r]-A[row][l-1])
                    else:
                        one_d_array.append(A[row][r])
                ans = max(ans, csum_less_than_k(one_d_array, k))

        return ans


class SolutionWrong:
    def maxSumSubmatrix(self, A: List[List[int]], k: int) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if j > 0:
                    A[i][j] += A[i][j - 1]  # only add columns of this row i
        # print(A)
        maxSubRect = -127 * 100 * 100  # lowest possible value
        res = -127 * 100 * 100
        for l in range(m):
            for r in range(l, m):
                subRect = 0
                for row in range(n):
                    if l > 0:  # max 1D Range Sum on columns in this row
                        subRect += A[row][r] - A[row][l - 1]
                    else:
                        subRect += A[row][r]
                    # if subRect < 0: #greedy, restart if running sum < 0
                    # print('is less')
                    # subRect = 0
                    # print(subRect)
                    maxSubRect = max(maxSubRect, subRect)  # Kadane's algo in rows
                    if maxSubRect <= k:
                        res = max(res, maxSubRect)
                    if subRect <= k:
                        res = max(res, subRect)

        return res


if __name__ == '__main__':
    s = Solution()
    s.maxSumSubmatrix([[5,-4,-3,4],[12,-4,4,5],[-7,1,5,-4]],8)