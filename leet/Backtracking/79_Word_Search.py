import collections
from typing import List

# O(n*3^L), n is number of cells in the board
# L is the length of the word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starts = collections.defaultdict(list)
        n = len(board)
        m = len(board[0])

        if n * m < len(word):
            return

        freq = collections.Counter(list(word))
        for line in board:
            for ch in line:
                if ch in freq:
                    freq[ch] -= 1
        for c in freq:
            if freq[c] > 0:
                return

        for i in range(n):
            for j in range(m):
                starts[board[i][j]].append((i, j))

        def helper(i, j, k):
            if k >= len(word):
                return True
            letter = board[i][j]
            board[i][j] = -1
            for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                x = dx + i
                y = dy + j
                if 0 <= x < n and 0 <= y < m and board[x][y] != -1 and board[x][y] == word[k]:
                    if helper(x, y, k + 1):
                        return True
            board[i][j] = letter
            return False

        if word[0] not in starts:
            return False

        for i, j in starts[word[0]]:
            if helper(i, j, 1):
                return True
        return False
