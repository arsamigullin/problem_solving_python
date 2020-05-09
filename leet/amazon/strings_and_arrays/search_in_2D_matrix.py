# this problem
# https://leetcode.com/problems/search-a-2d-matrix/submissions/

# similar problem
# search_in_2D_matrix_II.py - https://leetcode.com/problems/search-a-2d-matrix-ii/

import typing
List = typing.List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        NOTE: in this problem the first element of the next row is greater of the latest element of previous row
        We can notice that this array can be composed as sorted 1-dimensional array
        The problem is how to calculate the position in 2-dimensional having only the position of 1-dimensional array

        This must be remembered 
        Given position of 1-dimensional array i, to get the position of 2-dimensional array we do the following
        arr[i//column_count][i%column_count]

        The rest part of the code is regular Binary search
        '''
        if not matrix:
            return False
        lo = 0
        n = len(matrix)
        m = len(matrix[0])
        hi = m*n - 1
        while hi >= lo:
            mid_idx = (hi+lo)//2
            mid_elem = matrix[mid_idx//m][mid_idx%m]
            if mid_elem > target:
                hi = mid_idx - 1
            elif mid_elem < target:
                lo = mid_idx + 1
            else:
                return True
        return False





