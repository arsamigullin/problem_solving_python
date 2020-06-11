from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board:
            return 0
        n = len(board)
        m = len(board[0])
        cnt = 0
        # we check only left and top because we move from left-top direction to the bottom
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                # if being on the part of ship(meaning board[i][j] is 'X')
                # on the left we have part another part of ship
                if i-1>=0 and board[i-1][j] == 'X':
                    continue
                # on the top we have part another part of ship
                if j-1>=0 and board[i][j-1] == 'X':
                    continue
                # if no parts of the ship on the left and top
                # this is a separate ship
                cnt+=1
        return cnt