import collections
import typing
List = typing.List
class MySolution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        """
        Do not return anything, modify board in-place instead.
        """
        notflipped = []
        # this is complementary array
        visited = [['Y'] * len(board[0]) for _ in range(len(board))]
        i, j, di, dj = 0, 0, 0, 1
        # here we go over BORDER only and collect items that are going to be escaped
        for _ in range((len(board) + len(board[0])) * 2 - 3):
            if board[i][j] == 'O':
                notflipped.append((i, j))
            if j + dj == len(board[0]):
                di, dj = 1, 0
            elif i + di == len(board):
                di, dj = 0, -1
            elif j + dj < 0:
                di, dj = -1, 0
            elif i + di == 0 and j + dj == 0:
                break
            i += di
            j += dj

        q = collections.deque(notflipped)
        # we do BFS from collected escaped nodes
        # we mark element as '1' once it visited
        while q:
            x, y = q.popleft()
            visited[x][y] = '1'
            for rowOffset, colOffset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                a, b = x + rowOffset, y + colOffset
                if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == 'O' and visited[a][b] == 'Y':
                    q.append((a, b))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and visited[i][j] == 'Y':
                    board[i][j] = 'X'

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Step 1). retrieve all border cells
        from itertools import product
        borders = list(product(range(self.ROWS), [0, self.COLS-1])) \
                + list(product([0, self.ROWS-1], range(self.COLS)))

        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for row, col in borders:
            #self.DFS(board, row, col)
            self.BFS(board, row, col)

        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':   board[r][c] = 'X'  # captured
                elif board[r][c] == 'E': board[r][c] = 'O'  # escaped


    def BFS(self, board, row, col):
        from collections import deque
        queue = deque([(row, col)])
        while queue:
            (row, col) = queue.popleft()
            if board[row][col] != 'O':
                continue
            # mark this cell as escaped
            board[row][col] = 'E'
            # check its neighbor cells
            if col < self.COLS-1: queue.append((row, col+1))
            if row < self.ROWS-1: queue.append((row+1, col))
            if col > 0: queue.append((row, col-1))
            if row > 0: queue.append((row-1, col))

if __name__ == "__main__":
    s = Solution()
    s.solve([["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]])