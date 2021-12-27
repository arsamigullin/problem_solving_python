from typing import List

# examp: [6,6,0,1,1,4,6]
# after sorting [0, 1, 1, 4, 6, 6, 6]
# we can replace:
# 1. three largest items to nums[-4], min_val = nums[-4] - nums[0]
# 2. 2 largest items to the nums[-3] and 1 smallest items to the nums[1], min_val = nums[-3] - nums[1]
# 3. 1 largest item to the nums[-2] and 2 smallest items to the nums[2], min_val = nums[-2] - nums[2]
# 4. 3 smallest items to the nums[3], min_val = nums[-1] - nums[3]

# this is exact what is done here
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return min(b-a for a, b in zip(nums[:4],nums[-4:]))