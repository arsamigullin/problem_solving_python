from typing import List
# similar problems
# 525_contigious_array.py
# 209. Minimum Size Subarray Sum


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pref = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pref[i + 1] = pref[i] + nums[i]
        d = {}
        max_len = 0
        for i, p in enumerate(pref):
            if p - k in d:
                max_len = max(max_len, i - d[p - k])
            d.setdefault(p, i)
        return max_len
