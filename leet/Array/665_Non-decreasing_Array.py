from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        cnt = 0
        n = 0
        for i in range(1, len(nums)):
            if nums[i - 1] <= nums[i]:
                n = nums[i - 1]
            elif n <= nums[i]:
                cnt += 1
            else:
                nums[i] = nums[i - 1]
                cnt += 1
            if cnt > 1:
                return False

        return cnt <= 1