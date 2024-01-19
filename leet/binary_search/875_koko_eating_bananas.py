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

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        lo = 1
        hi = max(piles)

        def check(k):
            #print(k)
            #print(sum([p//k if p%k == 0 else (p//k)+1 for p in piles]))
            return sum([p//k if p%k == 0 else (p//k)+1 for p in piles]) > h

        while lo < hi:
            mid = (hi + lo)//2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        r = max(piles)
        if n == h:
            return r
        s = sum(piles)
        l = ceil(s/h)
        r = min(r, ceil(s/(h-n+1)))
        while l < r:
            m = (l + r) >> 1
            if sum(ceil(p/m) for p in piles) > h:
                l = m + 1
            else:
                r = m
        return l