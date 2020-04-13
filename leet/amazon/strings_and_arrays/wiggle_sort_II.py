#this problem
#https://leetcode.com/problems/wiggle-sort-ii/

# useful discussion
# https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof

import typing
List = typing.List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
if __name__ == "__main__":
    s = Solution()
    #s.wiggleSort([1,2,2,1,2,1,1,1,1,2,2,2])
    s.wiggleSort([4,5,5,6])