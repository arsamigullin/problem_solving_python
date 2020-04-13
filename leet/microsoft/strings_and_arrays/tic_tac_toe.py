# similar problem
# https://leetcode.com/problems/design-tic-tac-toe/
# 348. Design Tic-Tac-Toe

# https://leetcode.com/problems/valid-tic-tac-toe-state/
# 794. Valid Tic-Tac-Toe State

class TicTacToeMy:

    def __init__(self, n: int):
        """
        IMPORTANT: The win combinations is either whole row or whole column or one of the Central diagonals
        """
        self.grid = [[0] * n for _ in range(n)]
        self.n = n
        self.diag1 = self.__getdiagonal(0, 0, 1, 1) # determine first central diagonal
        self.diag2 = self.__getdiagonal(n - 1, 0, -1, 1) # determine second central diagonal
        self.shifts = [(0,1,0,-1), (1,0,-1,0)] # shifts represents movement over column and row

    def __getdiagonal(self, x, y, dx, dy):
        diag = set()
        for _ in range(self.n):
            diag.add((x,y))
            x+=dx
            y+=dy
        return  diag


    def move(self, row: int, col: int, player: int) -> int:

        self.grid[row][col] = player
        for shifts in self.shifts:
            # if we all the elements are the same on a row or column
            # the player won
            if self.find(shifts, row, col, player):
                return player
        # if current player is on one of the diagonals and all items of diagonals is the same
        # this player won
        if all(player == self.grid[i][j] for i, j in self.diag1) or all(player == self.grid[i][j] for i, j in self.diag2):
            return player
        # nobody won
        return 0

    def find(self, shifts, row, col, player):
        for i in range(0, len(shifts), 2):
            dx, dy = shifts[i], shifts[i + 1]
            x = row
            y = col
            while 0 <= x < self.n and 0 <= y < self.n:
                if self.grid[x][y] != player:
                    return False
                x += dx
                y += dy
        return True

class TicTacToeShort:

    # Time: O()
    # Space: O()
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row, self.col, self.diag, self.antidiag, self.n = [0] * n, [0] * n, 0, 0, n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        m = player * 2 - 3 # for different player this will have different sign
        # if all items of row of tic tac toe grid have the same value [0,1] [0,2] [0,3], ... [0,n]
        # self.row[row] will be equal n
        self.row[row] += m
        # if col of tic tac toe grid have the same value
        # self.col[col] will be equal n
        self.col[col] += m
        # if player on the main diagonal then row and col necessarily equal
        # this just collects the total value on the main diagonal
        if row == col: self.diag += m
        # if player on the second main diagonal than row + col == self.n-1
        # this just collects the total value on the second main diagonal
        if row + col == self.n - 1: self.antidiag += m

        if m * self.n in [self.row[row], self.col[col], self.diag, self.antidiag]: return player
        return 0

if __name__ == '__main__':

    s = TicTacToeShort(2)
    print(s.move(0, 1, 1))
    print(s.move(1, 1, 2))
    print(s.move(1, 0, 1))

    s = TicTacToeShort(2)
    print(s.move(0,0,2))
    print(s.move(0, 1, 1))
    print(s.move(1, 1, 2))