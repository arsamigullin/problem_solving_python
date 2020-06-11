from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        for k in range(len(nums)):
            i, j = k+1, len(nums)-1
            while i<j:
                threesum = nums[k] + nums[i] + nums[j]
                if target - threesum == 0:
                    return threesum
                # since we need to find closest sum
                # we must consider abs of the min diff and  target - threesum
                if abs(target - threesum) < abs(diff):
                    # but we want to store here real difference
                    diff = target - threesum

                if target > threesum:
                    i+=1
                else:
                    j-=1
        # to get this calculation correct
        return target - diff
