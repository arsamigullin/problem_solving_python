from bisect import bisect_right
from typing import List

matrix = [
   [1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

import heapq
# O(m*n+k*lg(n*m))
class SolutionMy:
    def kthSmallest(self, matrix: list, k: int) -> int:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(l, matrix[i][j])
        print(heapq.nsmallest(k, l))[-1]

#O(k * lg(n*m))
class SolutionHeap:
    def kthSmallest(self, matrix: list, k: int) -> int:
        heap=[]
        def push(i,j):
            if i<len(matrix) and j<len(matrix[0]):
                heapq.heappush(heap,(matrix[i][j],i,j))
        push(0,0)
        ksmallest = 0
        while heap and k>0:
            ksmallest, i, j = heapq.heappop(heap)
            push(i, j+1)
            if j == 0:
                push(i+1,j)
            k-=1
        return ksmallest

# O(lg(W)*n*lgn)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        length = len(matrix)

        left = matrix[0][0]
        right = matrix[length - 1][length - 1]

        while left < right:
            mid = left + (right - left) // 2
            print([bisect_right(row, mid) for row in matrix], mid)
            pos = sum(bisect_right(row, mid) for row in matrix)

            if pos < k:
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == "__main__":
    s = Solution()
    s.kthSmallest(matrix, 8)
    print('done')