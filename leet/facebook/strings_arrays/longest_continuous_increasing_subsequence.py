from typing import List
# this problem
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        _max = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                _max = max(_max, count)
                count = 1
        return max(_max, count)