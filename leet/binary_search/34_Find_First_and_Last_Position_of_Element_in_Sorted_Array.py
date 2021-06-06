from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return (-1, -1)
        lo = 0
        hi = len(nums)
        # this is bisec_right
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        r = lo
        # print(r)
        # r = bisect.bisect_right(nums, target)
        if nums[r - 1] != target:
            return (-1, -1)
        # l = bisect.bisect_left(nums[:r], target)
        # this is bisect_left
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo+(hi-lo)//2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        l = lo

        # print(l)
        return (l, r - 1)

