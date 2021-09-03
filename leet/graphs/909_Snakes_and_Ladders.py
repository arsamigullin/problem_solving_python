import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        mem = []
        n = len(board)
        m = len(board[0])
        i = 1
        rev = 0

        while i <= n * n:
            row = []
            for j in range(m):
                row.append(i)
                i += 1
            if rev:
                row.reverse()
            mem.append(row)
            rev ^= 1
        mem.reverse()

        d = collections.defaultdict(int)
        for i in range(n):
            for j in range(n):
                d[mem[i][j]] = (i, j)

        q = collections.deque([(n - 1, 0, 0)])
        visited = {1}
        while q:
            i, j, dist = q.popleft()
            curr = mem[i][j]
            for nxt in range(curr + 1, min(curr + 6, n * n) + 1):
                x, y = d[nxt]
                if nxt == n * n:
                    return dist + 1 if board[x][y] == -1 else -1
                if nxt not in visited:
                    if board[x][y] != -1:
                        x, y = d[board[x][y]]
                        if mem[x][y] == n * n:
                            return dist + 1 if board[x][y] == -1 else -1
                    q.append((x, y, dist + 1))
                    visited.add(nxt)

        return -1

if __name__ == '__main__':
    s = Solution()
    s.snakesAndLadders([[-1,4,-1],[6,2,6],[-1,3,-1]])
