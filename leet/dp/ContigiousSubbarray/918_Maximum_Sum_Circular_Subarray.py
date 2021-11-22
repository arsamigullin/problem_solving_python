# top solution
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max_end = nums[0]
        max_end = nums[0]
        cur_min_end = nums[0]
        min_end = nums[0]

        tot = sum(nums)

        for i in range(1, len(nums)):
            cur_max_end = max(nums[i], nums[i] + cur_max_end)
            max_end = max(max_end, cur_max_end)
            cur_min_end = min(nums[i], nums[i] + cur_min_end)
            min_end = min(min_end, cur_min_end)

        # this part tot - min_end if tot != min_end else tot is to avoid cases like
        # [-3,-2,-1]
        return max(max_end, tot - min_end if tot != min_end else tot)