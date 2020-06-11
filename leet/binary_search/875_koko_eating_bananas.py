from typing import List


class Solution1:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            cnt = sum((b + mid - 1) // mid for b in piles)
            if cnt > H:
                left = mid + 1
            else:
                right = mid

        return left


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lo = 1
        hi = max(piles)
        res = -1
        while lo <= hi:
            guess = lo + (hi - lo) // 2
            # this slows down the performance twice
            # spent_hours = sum(num//guess + min(1, num%guess!=0) for num in piles)
            spent_hours = sum((b + guess - 1) // guess for b in piles)
            if spent_hours > H:
                lo = guess + 1
            else:
                res = guess
                hi = guess - 1

        return res