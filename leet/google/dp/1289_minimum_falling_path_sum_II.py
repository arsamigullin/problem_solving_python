import heapq
from typing import List
# similar
# 256, 265, 931, 1289, 1937, 1014


class Solution:
    def minFallingPathSum(self, A):
        for i in range(len(A) - 1):
            r = heapq.nsmallest(2, A[i])
            for j in range(len(A[0])):
                A[i + 1][j] += r[1] if A[i][j] == r[0] else r[0]
        return min(A[-1])

    def minFallingPathSum2(self, A):
        for i in range(1, len(A)):
            r = heapq.nsmallest(2, A[i - 1])
            for j in range(len(A[0])):
                A[i][j] += r[1] if A[i - 1][j] == r[0] else r[0]
        return min(A[-1])