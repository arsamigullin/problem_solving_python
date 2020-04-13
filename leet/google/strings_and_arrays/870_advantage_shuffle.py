from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        indexedB = [(v, i) for i, v in enumerate(B)]
        indexedB.sort()
        ans = [0] * len(A)
        A.sort()
        j = 0
        for a in A:
            b, ind = indexedB[j]
            if a > b:
                ans[ind] = a
                j += 1
            else:
                b, ind = indexedB.pop()
                ans[ind] = a
        return ans

