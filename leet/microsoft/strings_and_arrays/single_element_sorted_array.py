import typing
List = typing.List
# Observation 
# once the single is met all the pairs the pairs are starting from odd index
# all pairs of numbers till 3 are starting from even indexes 
# starting from 4 the pairs are starting from odd (5)
# [ 1, 1, 2, 2, 3, 4, 4, 8, 8] - nums
# [ 0, 1, 2, 3, 4, 5, 6, 7, 8] - indexes
# 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0 
        e = len(nums) - 1

        while s < e:
            mid = e - (e-s)//2
            # if we've got to the odd index
            # we need to understand if we are to the left of single number
            # we decrease mid so it is now even num
            if mid % 2 == 1:
                mid = mid - 1
            # if val under mid and mid+1 are equal this means we are currently to the left of the single number
            # since this pair (nums[mid], nums[mid + 1]) is starting from even number
            if nums[mid] == nums[mid+1]:
                s = mid + 2
            else:
                e = mid 

        return nums[s]

if __name__ == "__main__":
    s = Solution()
    print(s.singleNonDuplicate([1,1,2,2,3,4,4,8,8]))