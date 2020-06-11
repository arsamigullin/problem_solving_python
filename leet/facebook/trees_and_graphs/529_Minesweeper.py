from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        n = len(board)
        m = len(board[0])
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def dfs(i, j):
            numMines = 0
            for di, dj in dirs:
                x = di + i
                y = dj + j
                if 0 <= x < n and 0 <= y < m and board[x][y] == "M":
                    numMines += 1
            # if we have mines in adjacent cells
            if numMines > 0:
                # put it here and return
                board[i][j] = str(numMines)
                return
            board[i][j] = 'B'
            # here we have unrevealed cells
            for di, dj in dirs:
                x = di + i
                y = dj + j
                # we want to visit only empty spaces 'E'
                if 0 <= x < n and 0 <= y < m and board[x][y] == 'E':
                    dfs(x, y)

        dfs(x, y)
        return board