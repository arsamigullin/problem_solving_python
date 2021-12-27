from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        lo = min(bloomDay)
        hi = max(bloomDay) + 1

        def possible(daysPassed):
            flowers = 0
            bouqets = 0
            for bd in bloomDay:
                # the current bloomday is greater daysPassed
                # resetting flowers
                if daysPassed < bd:
                    flowers = 0
                else:
                    # NOTE: bouqets are never reset
                    bouqets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
                if bouqets >= m:
                    return True
            return False
        # binary search over the min and max days
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
