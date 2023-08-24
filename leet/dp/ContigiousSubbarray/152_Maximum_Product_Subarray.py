from typing import List

# the key point here is CONTIGUOUS
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_max = nums[0]
        cur_min = nums[0]
        r = nums[0]
        for i in range(1, len(nums)):
            # [1,2,3,-4,-5]
            # up until num 3, cur_max will be 6
            # cur_min will be 3
            # At the -4 we will swap cur_max and cur_min
            # this is to make cur_min even smaller because 6 (former cur_max, now cur_min) * -4 = -24
            # At the -5 we do swap again to make cur_max even larger because -24 (former cur_min, now cur_max) * -5 = 120
            if nums[i]<0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i]) # this is regular code for CONTIGUOUS subarray
            cur_min = min(nums[i], cur_min * nums[i]) # this is regular code for CONTIGUOUS subarray
            r = max(r, cur_max) # this as well
        return r

if __name__ == '__main__':
    s = Solution()
    s.maxProduct([-10,-2,-3,-4,-5])
    s.maxProduct([-1,-2,-3,-4,-5])
    s.maxProduct([1,2,3,-4,-5])
    s.maxProduct([1, 2, -3, 2, -3])
    s.maxProduct([1,2,-3,4,-5])