from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bisect_left(arr, x):
            lo = 0
            hi = len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        heaters.sort()
        r = 0
        for h in houses:
            i = bisect_left(heaters, h)
            if i == 0:
                r = max(r, heaters[i] - h)
            elif i == len(heaters):
                r = max(r, h - heaters[i - 1])
            else:
                r = max(r, min(heaters[i] - h, h - heaters[i - 1]))
        return r
