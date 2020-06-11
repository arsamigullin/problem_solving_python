
# this problem
# search_in_2D_matrix_II.py - https://leetcode.com/problems/search-a-2d-matrix-ii/

# similar problem
# search_in_2D_matrix.py - https://leetcode.com/problems/search-a-2d-matrix/

import typing
List = typing.List

class Solution:
    #O(lg(n!))
    def searchMatrix(self, matrix, target):
        '''
        In this approach we do binary search while iterating over the main diagonal
        NOTE: main diagonal is the elements where i==j, i.e. [0,0],[1,1] and so on
        so the diagonal of matrix where m!=n will not connect left top and right bottom elements
        Neverthless, it is enough to cover the whole matrix by binary search
        Consider an example
        [1,7]
        [2,9]
        [3,11]
        the main diagonal has lenght two and consists of 1 and 9
        and we covering 3 and 11 here as well because we do binary search at first column(1,2,3) and at second column(7,9,11)
        '''

        def binary_search(start, target, vertical):
            '''
            NOTE: one each entering this function we reduce the search area
            since start is increasing every time
            '''
            lo = start
            hi = len(matrix[0])-1 if vertical else len(matrix)-1
        
            while hi>=lo:
                mid = hi - (hi - lo)//2
                '''
                vertical means we search in row by fixing this row, so only column index is changed
                '''
                if vertical:
                    if matrix[start][mid] == target:
                        return True
                    elif matrix[start][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    '''
                    Here we do search in column by fixing the column, so only row index is changed
                    '''
                    if matrix[mid][start] == target:
                        return True
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vert = binary_search(i, target, True)
            horiz = binary_search(i, target, False)
            if vert or horiz:
                return True
        return False


    def searchMatrix2(self, matrix, target):
        '''
        NOTE: 
        here we start from left bottom and if the first item is greater that target we decrease tge row
        because it is 100% that the target is not in the current row
        but if it is less than target we increase the column
        '''
        i = len(matrix) - 1
        j = 0

        while i >=0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i-=1
            else:
                j+=1
        return False


if __name__ == "__main__":
    s = Solution()
    s.searchMatrix(
    [[1,7],
    [2,9],
    [3,11]],11)
    s.searchMatrix(
  [[1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],50)