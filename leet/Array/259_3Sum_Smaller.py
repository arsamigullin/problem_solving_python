from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Sorting does not harm the condition i<j<k. you do not need to preserve the original index values but using each element once
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            lo = i + 1
            hi = n - 1
            t = target - nums[i]
            while lo < hi:
                # at this point we have triplet (i, lo, hi)
                if nums[lo] + nums[hi] >= t:
                    hi -= 1
                else:
                    # we cannot stop here because this is only number of triplets with (i, lo, lo+1 ... hi)
                    # we need move lo further to find the triplets (i, lo+1, lo+2 ... hi)
                    res += hi - lo
                    lo += 1
        return res
