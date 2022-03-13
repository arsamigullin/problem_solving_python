#https://leetcode.com/problems/search-in-rotated-sorted-array/

# algo
# 1. Use regular binary search
# 2. Check if the a[mid] >= a[start]
# 3. if so check if the target between start and mid i.e. [start]<=t<a[mid]. If so the end = mid -1 else start = mid + 1
#   doing start = mid + 1 we give it a try to findt a target since
class Solution:
    def search(self, nums: list, target: int) -> int:
        '''
        the skeleteon of searching target in rotated array is the same as for regular Binary Search
        (it has three cases target > nums[mid], target < nums[mid], target == nums[mid])
        The difference is that each case of first cases includes two cases to handle

        Let's consider an array [4,5,6,7,0,1,2]
        '''
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = end - (end - start)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[start]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1



if __name__ == "__main__":
    s = Solution()
    s.search([2, 4, 5, 6, 7, 0, 1], 1)
    s.search([4,5,6,7,0,1,2],6)