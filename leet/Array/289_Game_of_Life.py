from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        dp = [[board[i][j] for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                live = 0
                for dx, dy in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
                    if 0 <= i + dx < n and 0 <= j + dy < m:
                        #NOTE : here abs
                        live += int(abs(board[i + dx][j + dy]) == 1)

                # Rule 1 or Rule 3
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                # Rule 4
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                # if board[i][j] == 1 and live<2:
                #     board[i][j] = -1
                # elif board[i][j] == 1 and live > 3:
                #     board[i][j] = -1
                # elif board[i][j] == 1 and live in (2,3):
                #     board[i][j] = 2
                # elif board[i][j] == 0 and live ==3:
                #     board[i][j] = 2

        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
