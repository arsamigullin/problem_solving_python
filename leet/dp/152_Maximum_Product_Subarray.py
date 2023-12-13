from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        pos = -math.inf
        neg = math.inf
        # [2,-5,-2,-4,3]
        # 1 pos = 2 neg = 2 res=2
        # 2 swap pos=2 neg=2 then pos=max(-5,2*-5)=-5 neg=min(-5,2*-5)=-10 res=-5
        # 3 swap pos=-10 neg=-5 then pos=max(-2,-2*-10)=20 neg=min(-2,-5*-2)=-2 res=20
        # 4 swap pos=-2 neg=20 then pos=max(-4,-4*-2)=8 neg=min(-4,20*-4)=-80 ,res=20
        # 5 pos=max(3,3*8)=24 neg=min(3,3*-80)=-240 res=24
        res = -math.inf
        for i in range(n):
            if nums[i] < 0:
                pos, neg = neg, pos
            pos = max(nums[i], nums[i] * pos)
            neg = min(nums[i], nums[i] * neg)
            res = max(pos, res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.maxProduct([2,-5,-2,-4,3])