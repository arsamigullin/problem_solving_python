from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # this is a regular trie ds
        n = len(board)
        m = len(board[0])
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            # note: at the # key we store the entire word
            node['#'] = w

        res = []

        def backtracking(i, j, parent):
            letter = board[i][j]
            cur = parent[letter]

            word = cur.pop('#', False)
            # we do not stop here since it could be just a one word, we have to check other
            if word:
                res.append(word)

            # backtracking
            board[i][j] = '#'

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                x = dx + i
                y = dy + j
                if 0 <= x < n and 0 <= y < m and board[x][y] in cur:
                    backtracking(x, y, cur)
            # backtracking
            board[i][j] = letter

            if not cur:
                parent.pop(letter)

        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return res


