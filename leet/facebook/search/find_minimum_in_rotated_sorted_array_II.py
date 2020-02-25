#This problem
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

# The related problems
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# https://leetcode.com/problems/find-peak-element/


# Note:
# The array sorted and rotated
# In this problems no duplicates allowed
# There is a pivot point i where nums[i-1]>nums[i]<nums[i+1]
# Algo
# 1. find mid
# 2. Case nums[mid] < nums[end] means that mid behind the pivot point and we need to assign middle to the end
# 3. Case nums[mid] == nums[end] means we can before as well as bihind the pivot. We do not know for sure. Therefore we just 
#    decrement end
# 4. Otherwise mid before the pivot point, so the start will be s= mid + 1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0 
        e = len(nums) - 1
        while s < e:
            mid = s + (e-s)//2
            if nums[mid] < nums[e]:
                e = mid
            elif nums[mid] == nums[e]:
                e-=1
            else:
                s = mid + 1
        return nums[s]