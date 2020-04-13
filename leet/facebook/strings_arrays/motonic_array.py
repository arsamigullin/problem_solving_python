from typing import List
# this problem
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # wer are maintaining two variables inc and dec
        inc = dec = True
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                inc = False
            if A[i]<A[i+1]:
                dec = False
        return inc or dec