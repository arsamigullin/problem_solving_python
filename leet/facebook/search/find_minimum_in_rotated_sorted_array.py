#This problem
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# The related problems
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# https://leetcode.com/problems/find-peak-element/

# Note:
# The array sorted and rotated
# In this problems no duplicates allowed
# There is a pivot point i where nums[i-1]>nums[i]<nums[i+1]
# Algo
# 1. find mid
# 2. Case nums[mid] < nums[end] means that mid behind the pivot point and we need to assign middle to the end
# 3. Otherwise mid before the pivot point, so the start will be s= mid + 1
import typing
List = typing.List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0 
        e = len(nums) - 1

        while s <= e:
            mid = e - (e-s)//2
            if nums[s] < nums[mid] > nums[e]:
                s = mid + 1 
            else:
                e = mid - 1
        return nums[s]


if __name__ == "__main__":
    s = Solution()
    #s.findMin([3,4,5,1,2])
    s.findMin([4,5,6,7,0,1,2])
        