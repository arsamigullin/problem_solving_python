from typing import List


class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_val, min_val, error = max(nums), min(nums), float('inf')
        prev_mid = max_val
        while error > 0.00001:
            mid = (max_val + min_val) / 2
            if self.check(nums, mid, k):
                min_val = mid
            else:
                max_val = mid
            error = abs(prev_mid - mid)
            prev_mid = mid
        return min_val

    def check(self, nums, mid, k):
        prev, min_sum = 0, 0
        total = sum([nums[i] - mid for i in range(k)])
        if total >= 0:
            return True
        for i in range(k, len(nums)):
            total += nums[i] - mid
            prev += nums[i - k] - mid
            min_sum = min(min_sum, prev)
            if total > min_sum:
                return True
        return False


import numpy as np

class Solution2(object):
    def findMaxAverage(self, nums, k):
        lo, hi = min(nums), max(nums)
        nums = np.array([0] + nums)
        while hi - lo > 1e-5:
            mid = nums[0] = (lo + hi) / 2.
            sums = (nums - mid).cumsum()
            mins = np.minimum.accumulate(sums)
            if (sums[k:] - mins[:-k]).max() > 0:
                lo = mid
            else:
                hi = mid
        return lo