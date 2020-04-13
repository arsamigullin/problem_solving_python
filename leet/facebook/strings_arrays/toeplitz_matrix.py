# this problem
# https://leetcode.com/problems/toeplitz-matrix/
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        def helper(x, y):
            first = matrix[x][y]
            while x < n and y < m:
                if first != matrix[x][y]:
                    return False
                # diagonal is composed by increasing the current position by 1
                x += 1
                y += 1
            return True
        # we go over the top
        for j in range(m - 1):
            if not helper(0, j):
                return False
        #and left boundaries
        for i in range(1, n - 1):
            if not helper(i, 0):
                return False
        return True
