from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            max_cur = max(max_cur, cur)

        return max_cur