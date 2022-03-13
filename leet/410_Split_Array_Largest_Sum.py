import math
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        n = len(nums)
        memo = {}

        def helper(i, m):
            if i >= n:
                return 0
            if m == 0:
                return math.inf

            if (i, m) not in memo:
                res = math.inf
                cur = 0
                for j in range(i, n - m + 1):
                    cur += nums[j]
                    res = min(res, max(cur, helper(j + 1, m - 1)))
                memo[(i, m)] = res
            return memo[(i, m)]

        return helper(0, m)


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def canSplit(target):
            groups = 0
            cur = 0
            for num in nums:
                cur += num
                if cur > target:
                    groups += 1
                    cur = num
            return groups < m

        lo = max(nums)
        hi = sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canSplit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo