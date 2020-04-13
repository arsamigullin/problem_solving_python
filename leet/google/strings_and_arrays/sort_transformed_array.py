import heapq
import typing
List = typing.List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        def min_heapify(A, i):
            left = i * 2 + 1
            right = i * 2 + 2
            smallest = i
            if left < len(A) and A[left] < A[i]:
                smallest = left
            if right < len(A) and A[right] < A[smallest]:
                smallest = right
            if smallest != i:
                A[i], A[smallest] = A[smallest], A[i]
                min_heapify(A, smallest)

        def heappush(A, item):
            A.append(item)
            i = len(A) - 1
            while i >= 0 and A[i // 2] > A[i]:
                A[i], A[i // 2] = A[i // 2], A[i]
                i = i // 2

        def heappop(A):
            lastitem = A.pop()
            if A:
                returnitem = A[0]
                A[0] = lastitem
                min_heapify(A, 0)
                return returnitem
            return lastitem

        res = []
        for x in nums:
            heappush(res, a * x ** 2 + b * x + c)
        return [heappop(res) for _ in range(len(nums))]
if __name__ == "__main__":
    s = Solution()
    s.sortTransformedArray([-95,-95,-93,-92,-89,-89,-88,-82,-81,-79,-71,-71,-66,-66,-65,-65,-62,-61,-60,-54,-54,-51,-50,-48,-47,-45,-43,-37,-35,-35,-32,-32,-29,-24,-24,-22,-20,-20,-17,-14,-13,-12,-12,-4,1,8,11,14,16,16,22,24,26,28,28,28,29,30,31,36,44,46,49,60,60,60,62,64,65,73,76,86,87,89,91,92,93,94,94,96,96,97],41,
45,
-89)
    s.sortTransformedArray([-4,-2,2,4,6,10,12], 0, 1, 0)