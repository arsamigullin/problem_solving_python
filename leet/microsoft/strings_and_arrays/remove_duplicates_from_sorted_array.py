import typing
List = typing.List
# two pointers technique
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
            i += 1
        return j + 1
