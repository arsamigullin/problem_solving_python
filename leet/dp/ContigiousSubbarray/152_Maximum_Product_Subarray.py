from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_max = nums[0]
        cur_min = nums[0]
        r = nums[0]
        for i in range(1, len(nums)):
            # if the cur num is negative
            # it makes the bigger num smallest and the smallest num bigger
            if nums[i]<0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i]) # this is regular code for continious subarray
            cur_min = min(nums[i], cur_min * nums[i]) # this is regular code for continious subarray
            r = max(r, cur_max) # this as well
        return r