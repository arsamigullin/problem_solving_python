import math
from typing import List

import  bisect


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = 1
        hi = float('-inf')
        for n in nums:
            lo = min(lo, n)
            hi = max(hi, n)

        while lo < hi:
            div = lo + (hi - lo) // 2
            res = sum([math.ceil(n / div) for n in nums])
            if res > threshold:
                lo = div + 1
            else:
                hi = div

        return lo

if __name__ == '__main__':
    s = Solution()
    s.smallestDivisor([1,2,5,9], 6)