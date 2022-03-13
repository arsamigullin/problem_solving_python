from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        A = [0] * length
        for start, end, val in updates:
            A[start] += val
            if end < length - 1:
                A[end + 1] -= val

        for i in range(1, len(A)):
            A[i] += A[i - 1]
        return A