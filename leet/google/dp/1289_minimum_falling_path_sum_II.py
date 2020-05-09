from typing import List
# similar
# 256, 265, 931, 1289



class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        N = len(arr)
        M = len(arr[0])

        for n in range(1, N):
            first_min = second_min = None
            for m in range(M):
                cur = arr[n - 1][m]
                if first_min is None or cur < arr[n - 1][first_min]:
                    second_min = first_min
                    first_min = m
                elif second_min is None or cur < arr[n - 1][second_min]:
                    second_min = m
            for m in range(M):
                if m == first_min:
                    arr[n][m] += arr[n - 1][second_min]
                else:
                    arr[n][m] += arr[n - 1][first_min]
        return min(arr[-1])