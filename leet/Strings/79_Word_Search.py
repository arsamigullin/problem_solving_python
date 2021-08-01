# backtracking, optimized
import collections
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.wordlist = list(word)
        self.path = []
        col, row = len(board[0]), len(board)
        if col * row < len(word):
            return

        freq = collections.Counter(list(word))
        for line in board:
            for ch in line:
                if ch in freq:
                    freq[ch] -= 1
        for c in freq:
            if freq[c] > 0:
                return

        def backtracking(curr, row, col):
            y, x = curr
            if [y, x] in self.path or board[y][x] != self.wordlist[0]:
                return
            self.path.append([y, x])
            curr_word = self.wordlist.pop(0)
            if not self.wordlist:
                return True
            for x_, y_ in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= x + x_ < col and 0 <= y + y_ < row:
                    if backtracking([y + y_, x + x_], row, col):
                        return True
            self.wordlist.insert(0, curr_word)
            self.path.pop()

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtracking([i, j], row, col):
                        return True
        return False
