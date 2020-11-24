from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def rb(nums: List[int]) -> int:
            prevMax = 0
            curMax = 0
            for num in nums:
                temp = curMax
                curMax = max(prevMax + num, curMax)
                prevMax = temp
            return curMax

        return max(rb(nums[:len(nums) - 1]), rb(nums[1:]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        def helper(nums):
            prev_max = prev_prev_max = 0
            for n in nums:
                temp = prev_max
                prev_max = max(prev_prev_max + n, prev_max)
                prev_prev_max = temp
            return prev_max
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))

