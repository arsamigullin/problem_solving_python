import math
from typing import List


# Similar
# 325. Maximum Size Subarray Sum Equals k
# O(n)
# NOTE: of which the sum is greater than or equal to target
class Solution1:
    '''
    [1,2,3,4,5], s = 11
    it will reach 5 so the _sum is equal 15
    now we want to decrease _sum from the left
    Interations of internal loop
    1 iteration
    15>11
    max_len = i - previ + 1 = 4 - 0 + 1 = 5
    _sum = _sum - nums[previ] = 15 - 1 = 14
    previ = previ + 1 = 1


    2 iteration:
    14>11
    max_len = i - previ + 1 = 4 - 1 + 1= 4
    _sum = _sum - nums[previ] = 14 - 2 = 12
    previ = previ + 1 = 2

    3 iteration:
    12>11:
    max_len = i - previ + 1= 4-2+1=3
    _sum = _sum - nums[previ] = 12 - 3 = 9

    '''

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        _sum = 0
        previ = 0
        min_len = float('inf')
        for i, v in enumerate(nums):
            _sum += v
            # NOTE: instead of calculating previ and then calculate min_len
            # we calculate min_len each iteration of while
            while _sum >= s:
                min_len = min(min_len, i - previ + 1)
                _sum -= nums[previ]
                previ += 1
        return 0 if min_len == float('inf') else min_len


# O(NlogN) solution
class Solution2:
    '''
    The key point is prefix sum makes a positive array to be sorted
    we can gain from it
    '''

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        _sum = 0
        min_len = float('inf')
        pref = [0] * (len(nums) + 1)

        def binarysearch(lo, hi, target):
            res = -1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if target >= pref[mid]:
                    res = mid
                    lo = mid + 1
                else:
                    hi = mid
            return res

        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] + nums[i]
            if pref[i + 1] - s >= 0:
                j = binarysearch(0, i + 1, pref[i + 1] - s)
                min_len = min(min_len, i - j + 1)
        return 0 if min_len == float('inf') else min_len


class Solution3:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        def bisect_left(lo, hi, t, A):

            while lo < hi:
                mid = lo + (hi - lo) // 2
                if A[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        pref = [0] * (len(nums) + 1)
        min_len = math.inf

        for i, a in enumerate(nums):
            pref[i + 1] = pref[i] + a
        print(pref)
        for i, a in enumerate(nums):
            if pref[i + 1] - target >= 0:
                j = bisect_left(0, len(pref), pref[i + 1] - target, pref)
                min_len = min(min_len, i - j + 1)
        return 0 if min_len == math.inf else min_len


if __name__ == '__main__':
    s = Solution3()
    s.minSubArrayLen(11,[1,2,3,4,5])
    s.minSubArrayLen(7,[2,3,1,2,4,3])