from typing import List

# subarray should be contiguous
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-3+1):
            if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
                # we could think of it as number of arithmetic slices (contiguous subarray)
                # i.e [1,3,5,7,9], 1,3,5 is 1st, 3,5,7 is 2nd and 5,7,9 is 3rd
                # that means in the 1st iteration cur is 1,
                # on the second cur is 2
                # on the third cur is 3
                # the res is sum of all cur, i.e. 1+2+3
                cur = cur + 1
                res += cur
            else:
                cur = 0
        return res