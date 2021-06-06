import collections
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


class SolutionMy:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = [0] * n
        cols = [0] * n
        grid = [['.'] * n for _ in range(n)]
        # here we check no Q is sitting at the diagonals
        def checkdiag(i, j):
            x, y = i, j
            while x < n and y < n:
                if grid[x][y] == 'Q':
                    return False
                x += 1
                y += 1

            x, y = i, j
            while x >= 0 and y >= 0:
                if grid[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1

            x, y = i, j
            while x >= 0 and y < n:
                if grid[x][y] == 'Q':
                    return False
                x -= 1
                y += 1

            x, y = i, j
            while x < n and y >= 0:
                if grid[x][y] == 'Q':
                    return False
                x += 1
                y -= 1

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
                    grid[i][j] = 'Q'
                    helper(i + 1)
                    rows[i] -= 1
                    cols[j] -= 1
                    grid[i][j] = '.'

        helper(0)
        return res


class SolutionT:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        rows = [0] * n
        cols = [0] * n
        diag = collections.defaultdict(int)
        op_diag = collections.defaultdict(int)
        res = []

        def helper(i):
            if i >= n:
                res.append([''.join(b) for b in board])
                return
            for j in range(n):
                if rows[i] == 0 and cols[j] == 0 and diag[j - i] == 0 and op_diag[j + i] == 0:
                    rows[i] = 1
                    cols[j] = 1
                    diag[j - i] = 1
                    op_diag[j + i] = 1
                    board[i][j] = 'Q'
                    helper(i + 1)
                    board[i][j] = '.'
                    rows[i] = 0
                    cols[j] = 0
                    diag[j - i] = 0
                    op_diag[j + i] = 0

        helper(0)
        return res

if __name__ == '__main__':
    s = SolutionT()
    s.solveNQueens(4)

