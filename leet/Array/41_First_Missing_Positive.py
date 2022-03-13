import math
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        left = math.inf
        right = math.inf
        for n in nums:
            if n <= 0:
                continue
            if n == 1:
                if n + 1 not in s:
                    left = min(left, n + 1)
                continue
            if n - 1 not in s:
                right = min(right, n - 1)
            if n + 1 not in s:
                left = min(left, n + 1)

        if left <= right:
            if left - 1 not in s:
                return 1
            else:
                return left
        else:
            if right - 1 in s:
                return right
            else:
                return 1

