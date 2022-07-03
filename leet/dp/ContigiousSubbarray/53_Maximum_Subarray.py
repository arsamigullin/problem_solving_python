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

# Time complexity
# The problem can be represented as the following recurrence T(n)=2T(n/2) + n^c = T(n)=2T(n/2) + O(n)
# Which means, on each iteration we need to solve 2 problems of size n/2, i.e. a=2 and b=n/2
# We also do additional O(1) work
# This is the second case of the Master theorem and
# if logba==c, logba = 1 because 2^1=2. c is also 1
# Time Complexity O(NlogN)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def helper(A, i, j):
            if i == j:
                return A[i]

            mid = (i + j) // 2
            s = 0
            left = -math.inf

            # this is additional work
            for k in range(mid, i - 1, -1):
                s += A[k]
                left = max(left, s)

            # this is additional work
            s = 0
            right = -math.inf
            for k in range(mid + 1, j + 1):
                s += A[k]
                right = max(right, s)

            lr = max(helper(A, i, mid), helper(A, mid + 1, j))

            return max(lr, left + right)

        return helper(nums, 0, len(nums) - 1)
