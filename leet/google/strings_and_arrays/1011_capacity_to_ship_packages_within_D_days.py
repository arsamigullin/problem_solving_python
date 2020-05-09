import math
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_wei = max(weights)
        # by some reason this function runs faster
        def canFit(cap):
            if cap < max_wei:
                return False
            cur = 0
            days = 0
            for weight in weights:
                cur += weight
                if cur > cap:
                    days += 1
                    cur = weight
                    if days > D:
                        return False
            days += 1
            if days > D:
                return False
            return True
        # this runs a bit slower
        def possible(guess):
            if guess < max_wei:
                return False
            days = 0
            pkg = 0
            for w in weights:
                if pkg + w > guess:
                    days += 1
                    pkg = 0
                if days > D:
                    return False
                pkg += w

            return days + 1 <= D
        # regarding low and high limits
        # the low boundary is the lowest values of weights
        lo = min(weights)
        # the highest values cannot be that count fo packages per day multiplied to the max_wei
        # [1,2,3,4,5], D = 2
        # lo is 1
        #  max is 5.
        # it is not possible to ship math.ceil(len(weights) // D) packages 
        hi = math.ceil(len(weights) // D) * max_wei # this is max ship capacity to ship packages for given D days


        # this both are working good binary searches
        # res = 0
        # while lo < hi:
        #     mid = (lo+hi)//2
        #     if possible(mid):
        #         hi = mid
        #     else:
        #         lo = mid+1
        # res = 0
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if possible(mid):
                hi = mid - 1
                res = mid
            else:
                lo = mid
        return res


if __name__ == '__main__':
    s = Solution()
    s.shipWithinDays([1,2,3,1,1],4)
    s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)