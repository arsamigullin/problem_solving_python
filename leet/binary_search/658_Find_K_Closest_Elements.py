import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k

        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


class Solution:
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