# this problem
# https://leetcode.com/problems/find-pivot-index/
# classic prefix sum problem
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = [0] * (len(nums)+1)
        for i in range(len(nums)):
            pref[i+1] = pref[i] + nums[i]
        for i in range(1, len(pref)):
            if pref[i-1] == pref[-1] - pref[i]:
                return i-1
        return -1