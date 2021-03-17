import collections
from typing import List

#duplicate number

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        miss = 0
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dup = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                miss = i + 1

        return [dup, miss]


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = collections.Counter(nums)
        res = [0,0]
        for i in range(n+1):
            if c[i] == 2:
                res[0] = i
            elif c[i] == 0:
                res[1] = i
        return res