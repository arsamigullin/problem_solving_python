# Candane algorithm
# Divide and Conquer
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            max_cur = max(max_cur, cur)

        return max_cur

# divide and conquer
# A = [-2,1,-3,4,-1,2,1,-5,4]
# Idea:
# 1. in each iteration divide array into two
# 2. find max of left and right sides. NOTE: we start from mid to left and from mid to right.
# This is because we want to find contiguous subarray to the left starting from mid and contiguous
# subarray to the right starting from mid. These both arrays compose contiguous subarrays at the middle
# 3. Proceed further with an unexplored i and j, i.e helper(i, mid) and helper(mid+1, j)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def helper(A, i, j):
            if i == j:
                return A[i]

            mid = (i + j) // 2
            s = 0
            left = -math.inf

            for k in range(mid, i - 1, -1):
                s += A[k]
                left = max(left, s)

            s = 0
            right = -math.inf
            for k in range(mid + 1, j + 1):
                s += A[k]
                right = max(right, s)

            lr = max(helper(A, i, mid), helper(A, mid + 1, j))

            return max(lr, left + right)

        return helper(nums, 0, len(nums) - 1)
