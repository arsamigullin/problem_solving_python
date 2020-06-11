from typing import List
# https://leetcode.com/problems/valid-tic-tac-toe-state/
# 794. Valid Tic-Tac-Toe State

# similar problem
# https://leetcode.com/problems/design-tic-tac-toe/
# 348. design Tic-Tac-Toe

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        bdiag = 0
        cnt_o = 0
        cnt_x = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    sign = -1
                    cnt_o += 1
                elif board[i][j] == 'X':
                    sign = 1
                    cnt_x += 1
                else:
                    continue
                rows[i] += sign
                cols[j] += sign
                if i == j:
                    diag += sign
                if i + j == 2:
                    bdiag += sign
        # it is impossible to have this state
        # ["XXX","XXO","OO "] or ["XXX","OOO","OO "]
        # so count of O must be the same or differ to 1
        if cnt_o not in {cnt_x, cnt_x - 1}: return False
        # this means once X forms winning combination no O should be left on the board (count of O must equal cnt_x - 1)
        # [XXX,XOO,OO]
        if (3 in rows or 3 in cols or 3 == diag or 3 == bdiag) and cnt_o != cnt_x - 1:
            return False
        # this means once O forms winning combination no O should be left on the board (count of O must equal cnt_x)
        # [XXX,OOO,XO]
        if (-3 in rows or -3 in cols or -3 == diag or -3 == bdiag) and cnt_o != cnt_x:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.validTicTacToe(["XXX","XOO","OO "])