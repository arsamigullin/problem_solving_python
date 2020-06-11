from typing import List

# interval
# interval intersection
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

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i]
            b1, b2 = B[j]
            if a2 < b1:
                i += 1
            elif b2 < a1:
                j += 1
            else:
                res.append((max(a1, b1), min(a2, b2)))
                if a2 <= b2:
                    i += 1
                if b2 <= a2:
                    j += 1
        return res

class Solution:
    def intervalIntersection(self, A: list, B: list) -> list:
        i, j = 0, 0

        res = []
        while i < len(A) and j < len(B):
            starta, enda = A[i]
            startb, endb = B[j]
            # if no intersection and interval A is behind interval B
            if enda < startb:
                i += 1
                continue
            # if no intersection and interval B is behind interval A
            elif starta > endb:
                j += 1
                continue
            # intersection is going to be max of starts and minimum of ends
            res.append([max(starta, startb), min(enda, endb)])
            # if there is an intersection and interval B is behind interval A
            if enda > endb:
                j += 1
            # if there is an intersection and interval A is behind interval B
            elif enda < endb:
                i += 1
            else:
                # we increase two pointers only if two intervals are ending with the same number
                i += 1
                j += 1
        return res



