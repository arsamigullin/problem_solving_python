from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n-1
        cnt = 0
        while i<j:
            if nums[i]<nums[j]:
                nums[i+1]+=nums[i]
                i+=1
                cnt += 1
            elif nums[i]>nums[j]:
                nums[j-1]+=nums[j]
                j-=1
                cnt+=1
            else:
                i+=1
                j-=1
        return cnt
