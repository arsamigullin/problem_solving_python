from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        # [0,1,-2,-3,-4]
        # 0. pos=0 neg=0 tot=0
        # 1. pos=1 neg=0 tot=1
        # 2. swap pos=0 neg=2 tot=1 this is where neg got increased, the product of subarray is negative [0,1,-2]
        # 3. swap pos=3 neg=1 tot=3 neg count turned to pos count
        # 4. swap pos=2 neg=4 tot=3
        # res=3

        # this example shows why we need neg + 1 if neg > 0 else 0
        # the first item is -1, we should not increase pos
        # [-1,2,3,-4]
        pos = 0
        neg = 0
        tot = 0
        for n in nums:
            if n > 0:
                pos, neg = pos + 1, neg + 1 if neg > 0 else 0
            elif n < 0:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                pos, neg = 0, 0
            tot = max(tot, pos)
        return tot

