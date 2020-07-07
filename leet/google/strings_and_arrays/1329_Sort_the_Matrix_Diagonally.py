import collections
from heapq import heapify, heappop
from typing import List


class SolutionMy:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        def sort(i, j):
            heap = []
            x, y = i, j
            while x < n and y < m:
                heap.append(mat[x][y])
                x += 1
                y += 1
            heapify(heap)
            x, y = i, j
            while x < n and y < m:
                mat[x][y] = heappop(heap)
                x += 1
                y += 1

        for i in range(n):
            sort(i, 0)
        for j in range(1, m):
            sort(0, j)
        return mat


class Solution1:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        for i in range(row - 1):
            vals = sorted([mat[i + k][k] for k in range(min(row - i, col))])
            for k in range(min(row - i, col)):
                mat[i + k][k] = vals[k]
        for j in list(range(col - 1))[1:]:
            vals = sorted([mat[k][j + k] for k in range(min(row, col - j))])
            for k in range(min(row, col - j)):
                mat[k][j + k] = vals[k]
        return mat


class SolutionDaleDiagonalTracking:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                # for dale diagonal we do subtract i-j
                # each diagonal has the same value
                d[i - j].append(mat[i][j])
        for i in d:
            d[i].sort()

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat[i][j] = d[i - j][0]
                d[i - j].pop(0)
        return mat