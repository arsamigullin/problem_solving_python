from typing import List


class Solution:
    '''
    # O(N!)
    THE KEY POINT to the solution is how to understand in O(1) that the diagonal is already busy
    For dale diagonal i-j defines the numbers of dale diagonal
    For hill diagonal i+j defines the numbers of hill diagonal
    This is example
    [
        [0,1,2],
        [-1,0,1]
        [-2,-1,0]
    ]

    each diagonal has the same value
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = [0] * n
        cols = [0] * n
        grid = [['.'] * n for _ in range(n)]
        dale_dict = set()
        hill_dict = set()

        def checkdiag(i, j):
            dale = i - j
            hill = i + j
            if dale in dale_dict:
                return False
            if hill in hill_dict:
                return False
            return True

        res = []

        def helper(i):
            if i == n:
                res.append([''.join(arr) for arr in grid])
                return
            for j in range(n):
                if rows[i] == 0 and cols[j] == 0 and checkdiag(i, j):
                    rows[i] += 1
                    cols[j] += 1
                    dale_dict.add(i - j)
                    hill_dict.add(i + j)
                    grid[i][j] = 'Q'
                    helper(i + 1)
                    dale_dict.discard(i - j)
                    hill_dict.discard(i + j)
                    rows[i] -= 1
                    cols[j] -= 1
                    grid[i][j] = '.'

        helper(0)
        return res


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(row = 0, hills = 0, next_row = 0, dales = 0, count = 0):
            """
            :type row: current row to place the queen
            :type hills: "hill" diagonals occupation [1 = taken, 0 = free]
            :type next_row: free and taken slots for the next row [1 = taken, 0 = free]
            :type dales: "dale" diagonals occupation [1 = taken, 0 = free]
            :rtype: number of all possible solutions
            """
            if row == n:  # if all n queens are already placed
                count += 1  # we found one more solution
            else:
                # free columns in the current row
                # ! 0 and 1 are inversed with respect to hills, next_row and dales
                # [0 = taken, 1 = free]
                free_columns = columns & ~(hills | next_row | dales)

                # while there's still a column to place next queen
                while free_columns:
                    # the first bit '1' in a binary form of free_columns
                    # on this column we will place the current queen
                    curr_column = - free_columns & free_columns

                    # place the queen
                    # and exclude the column where the queen is placed
                    free_columns ^= curr_column

                    count = backtrack(row + 1,
                                      (hills | curr_column) << 1,
                                      next_row | curr_column,
                                      (dales | curr_column) >> 1,
                                      count)
            return count

        # all columns available for this board,
        # i.e. n times '1' in binary representation
        # bin(cols) = 0b1111 for n = 4, bin(cols) = 0b111 for n = 3
        # [1 = available]
        columns = (1 << n) - 1
        return backtrack()
