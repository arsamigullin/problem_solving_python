from typing import List

# swap means for the ith element in A and B, the minimum swaps if we swap A[i] and B[i]
# non_swap means for the ith element in A and B, the minimum swaps if we DO NOT swap A[i] and B[i]

# from the problem description
# "The test cases are generated so that the given input always makes it possible."
# so this test case would not be possible, meaning that in this test case it is not possible to do
# the swap operations so that both arrays are strictly increasing
# A = [5, 9]
# B = [4, 3]
# Thus it does not matter the priority of the conditions. This could come first elif A[i-1]>=A[i] or B[i-1]>=B[i]
# However, if we fall under the first conditions
# A[i-1] >= B[i] or B[i-1]>=A[i] that means the both arrays are strictly in increasing order so far


# let's define below:
# swapRecord[i]: min swaps to make A[0: i] and B[0:i] increasing if we swap A[i] and B[i]
# fixRecord[i]: min swaps to make A[0: i] and B[0:i] increasing if we do not swap A[i] and B[i]
# if A[i - 1] >= A[i] or B[i - 1] >= B[i]:
# => we must have A[i - 1] < B[i] and B[i - 1] < A[i], otherwise we have no solution. For example:
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = 1
        non_swap = 0
        for i in range(1, n):
            if A[i-1] >= B[i] or B[i-1]>=A[i]:
                swap+=1
            elif A[i-1]>=A[i] or B[i-1]>=B[i]:
                swap, non_swap = non_swap + 1, swap
            else:
                min_swap = min(swap, non_swap)
                swap = min_swap + 1
                non_swap = min_swap
        return min(non_swap, swap)

if __name__ == '__main__':
    s = Solution()
    s.minSwap([8,10, 10, 11], [5, 7, 11, 14]) # this test case to explain why do we need the first condition
    s.minSwap([0, 3, 4, 9, 10], [2, 3, 7, 5, 6])