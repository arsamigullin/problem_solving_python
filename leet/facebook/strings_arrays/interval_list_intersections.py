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