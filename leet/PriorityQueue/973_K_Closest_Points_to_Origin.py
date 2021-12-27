import math
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def rand_partition(A, l, r):
            p = l+(r-l)//2 #random.randint(l, r)
            A[l], A[p] = A[p], A[l]
            p = A[l][0]
            m = l
            for k in range(l + 1, r + 1):
                if A[k][0] < p:
                    m += 1
                    A[k], A[m] = A[m], A[k]
            A[l], A[m] = A[m], A[l]
            return m

        result = []

        def quick_select(A, l, r, k):
            nonlocal result
            if l == r:
                result = [points[i] for num, i in A[:l+1]]
                return A[l]
            q = rand_partition(A, l, r)
            if q + 1 == k:
                result = [points[i] for num, i in A[:q+1]]
                return A[q]
            elif q + 1 > k:
                return quick_select(A, l, q - 1, k)
            else:
                return quick_select(A, q + 1, r, k)

        A = [(math.sqrt(x ** 2 + y ** 2), i) for i, (x, y) in enumerate(points)]
        quick_select(A, 0, len(A) - 1, k)
        return result
        # print(quick_select(A,0,7,8))
if __name__ == '__main__':
    s = Solution()
    s.kClosest([[6,10],[-3,3],[-2,5],[0,2]],3)
    #s.kClosest([[0,1],[1,0]],2)
    #s.kClosest([[1,3],[-2,2]], 1)