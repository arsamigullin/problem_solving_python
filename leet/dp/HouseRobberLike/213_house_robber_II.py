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

# the same as house robber 1 but we need to call the function twice
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def bob(start, end) -> int:
            curMax = 0
            prevMax = 0
            for i in range(start, end):
                prevMax, curMax = curMax, max(prevMax + nums[i], curMax)
            return curMax

        return max(bob(0, n - 1), bob(1, n))