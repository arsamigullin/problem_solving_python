#https://leetcode.com/problems/search-in-rotated-sorted-array/

# algo
# 1. Use regular binary search
# 2. Check if the a[mid] >= a[start]
# 3. if so check if the target between start and mid i.e. [start]<=t<a[mid]. If so the end = mid -1 else start = mid + 1
#   doing start = mid + 1 we give it a try to findt a target since
class Solution:
    def search(self, nums: list, target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = end - (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target<=nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1