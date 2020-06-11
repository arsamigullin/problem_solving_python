from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])

        # if first element of the row is 0 swap all the elements of that row
        # since it will bring max result
        # example, 1000(8) > 0111(7)
        # so, if we have 0111 we should swap it to have 1000(8)
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] ^= 1

        # if zero count in the column is greater m (count of elements in column)
        # swap the whole column, because the most count of zero will turn to the most count of 1
        # which will maximize the result
        for j, a in enumerate(list(zip(*A))):
            zercnt = a.count(0)
            if zercnt > n - zercnt:
                for i in range(n):
                    A[i][j] ^= 1
        # now our matrix is ready to be converted to int (i.e. we convert each row into integer)
        # A[i] is the whole row with m elements
        return sum(int(''.join(list(map(str, A[i]))), 2) for i in range(n))