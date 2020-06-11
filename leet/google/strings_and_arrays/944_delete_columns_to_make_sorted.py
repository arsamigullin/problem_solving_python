from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in zip(*A):
            if sorted(i) != list(i):
                count += 1
        return count

class SolutionMy:
    def minDeletionSize(self, A: List[str]) -> int:
        cols = len(A[0])
        cnt = 0
        for j in range(cols):
            for i in range(len(A)-1):
                if A[i][j]>A[i+1][j]:
                    cnt+=1
                    break
        return cnt