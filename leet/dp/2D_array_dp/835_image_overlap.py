import collections
from typing import List

# image rotation
# similar 750 Number Of Corner Rectangles

class Solution(object):
    def largestOverlap(self, A, B):
        N = len(A)
        count = collections.Counter()
        for i, row in enumerate(A):
            for j, v in enumerate(row):
                # for each 1 in A
                if v:
                    for i2, row2 in enumerate(B):
                        for j2, v2 in enumerate(row2):
                            # and for each 1 in B
                            # we increase counter
                            # A =[1,1]
                            #    [0,0]
                            # B =[0,0]
                            #    [1,1]
                            # for 1 in A with coordinates (0,0)
                            # for 1 in B with coordinates (1,0)
                            # (0,0)-(1,0) = -1, 0
                            # for 1 in A with coordinates (0,0)
                            # for 1 in B with coordinates (1,1)
                            # (0,0)-(1,1) = -1, -1
                            # for 1 in A with coordinates (0,1)
                            # for 1 in B with coordinates (1,0)
                            # (0,1)-(1,0) = -1, 1
                            # for 1 in A with coordinates (0,1)
                            # for 1 in B with coordinates (1,1)
                            # (0,1)-(1,1) = -1, 0

                            # Note we have two (-1,0) in counter, so the maximum is 2


                            if v2:
                                count[i-i2, j-j2] += 1
        return max(count.values() or [0])


class Solution2:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        max_overlap = 0
        for i, j in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

            x, y = 0, 0
            n, m = len(A), len(A[0])
            time = 1
            while x < n and y < m:
                print(x,y,n,m,i,j)
                if i < 0:
                    x += abs(i)
                else:
                    n -= i
                if j < 0:
                    y += abs(j)
                else:
                    m -= j

                count = 0
                for p in range(x, n):
                    for q in range(y, m):
                        if A[p][q] == B[p + i * time][q + j * time] == 1:
                            count += 1
                max_overlap = max(max_overlap, count)
                time+=1
                if i==0 and j==0:
                    break

        return max_overlap


class Solution1:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        max_overlap = 0
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            x,y = 0,0
            n,m = len(A), len(A[0])
            if i<0:
                x = 1
            else:
                n-=1
            if j<0:
                y=1
            else:
                m-=1

            count = 0
            for p in range(x, n):
                for q in range(y, m):
                    if A[p][q] == B[p + i][q + j] == 1:
                        count += 1
            max_overlap = max(max_overlap, count)

            #print(i,j,"__",x1,y1,n1,m1,"__",x2,y2,n2,m2)
        return max_overlap

if __name__ == '__main__':
    s = Solution()
    s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]],
                     [[0, 0, 0], [0, 1, 1], [0, 0, 1]])
    s.largestOverlap([[1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0],[0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0],[0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1],[0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0],[0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0],[1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0],[0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,1],[0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0],[0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0]],
[[0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0],[0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0],[0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,1],[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0],[1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0],[1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0],[0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0],[0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1],[1,0,0,1,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1],[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],[1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1],[0,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0],[0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0]])