import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        lo = 0
        hi = len(arr) - k
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # the goal is to minimize difference between
            # x - arr[mid] and arr[mid + k] - x
            # that is why when x - arr[mid] > arr[mid + k] - x we want to move search window to the right
            # that means x is more far from lo than from hi
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a = [(abs(v - x), v) for v in arr]
        heapq.heapify(a)
        result = []
        while a and k > 0:
            dif, elem = heapq.heappop(a)
            result.append(elem)
            k -= 1
        return sorted(result)

if __name__ == '__main__':
    s = Solution()
    s.findClosestElements([1,2,3,4,5],4,3)