from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            p,q = 0, len(A[0])-1
            # reverse the horizontal array
            while p<=q:
                A[i][p], A[i][q] = A[i][q], A[i][p]
                # do not forget to flip the image
                if p!=q:
                    A[i][p]^=1
                A[i][q]^=1
                p+=1
                q-=1
        return A