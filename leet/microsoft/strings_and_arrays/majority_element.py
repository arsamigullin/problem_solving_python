# this is 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = 0
        value = 0
        for i in range(len(nums)):
            if size == 0:
                value = nums[i]
                size += 1
            elif value == nums[i]:
                size +=1
            elif value != nums[i]:
                size-=1
        return value