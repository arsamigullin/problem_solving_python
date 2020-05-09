# this has the same approah
# 240. Search a 2D Matrix II

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
   def get(self, x: int, y: int) -> int:
       pass
   def dimensions(self) -> list[]:
       pass
# O(n*Logm)
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()

        def binarySearch(r):
            lo = 0
            hi = m - 1
            res = -1
            while lo <= hi:
                mid = hi - (hi - lo) // 2
                if binaryMatrix.get(r, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return lo if lo < m else -1

        res = float('inf')
        for i in range(n):
            val = binarySearch(i)
            if val >= 0:
                res = min(res, val)

        return -1 if res == float('inf') else res

#
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        x, y = binaryMatrix.dimensions()

        def seems_legit(column):
            return any(binaryMatrix.get(i, column) for i in range(x))

        lo = 0
        hi = y

        while lo < hi:
            mid = (lo + hi) // 2
            if seems_legit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < y else -1

# O(m+n)
class Solution:
    '''
    since each row is sorted and matrix contains only 0 and 1
    we can start from the top right corner and move to the left once we've met 1
    and move down once we've met 0
    [
        [0,1,1,1]
        [0,1,1,1]
        [1,1,1,1]
    ]
    this works because  each row is sorted that means we will go down only after reaching the very first 1
    in this row (and we will note it) then we never return to the right and if no 1's below are found
    we already have that we noted previously

    '''
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        x, y = 0, m - 1
        latestColumn = -1
        while x < n and y >= 0:
            if binaryMatrix.get(x, y) == 1:
                latestColumn = y
                y -= 1
            else:
                x += 1
        return latestColumn

