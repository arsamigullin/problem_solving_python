from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mins = [0]*n
        maxs = [0]*n
        for i in range(n-1,-1,-1):
            mins[i]=min(nums[i], mins[i+1] if i+1<n else nums[i])
        for i in range(n):
            maxs[i]=max(nums[i], maxs[i-1] if i-1>=0 else nums[i])
        for i in range(n-1):
            # Note: here we compare the current max element
            # and NEXT min element
            if maxs[i] <= mins[i+1]:
                return i+1
        return 1