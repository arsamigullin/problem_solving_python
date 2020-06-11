from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i<len(A) and j<len(B):
            a1, a2 = A[i]
            b1, b2 = B[j]
            # this is how we are searching for interval intersection
            lo = max(a1, b1)
            hi = min(a2, b2)
            if lo<=hi:
                res.append((lo, hi))
            if a2 > b2:
                j+=1
            else:
                i+=1
        return res