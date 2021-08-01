import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        n = len(mat)
        heap = []
        # here we add the first column of the matrix
        # think of it as merging two sorted arrays
        for r in range(min(n, k)):
            heap.append((mat[r][0], r, 0))

        heapq.heapify(heap)

        while k > 0:
            val, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (mat[r][c + 1], r, c + 1))
            k -= 1

        return val


class BinarySearchSolution:

    def countLessEqual(self, matrix, mid, smaller, larger):

        count, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:

                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1

            else:

                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid

                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

            count, smaller, larger = self.countLessEqual(matrix, mid, smaller, larger)

            if count == k:
                return smaller
            if count < k:
                start = larger  # search higher
            else:
                end = smaller  # search lower

        return start