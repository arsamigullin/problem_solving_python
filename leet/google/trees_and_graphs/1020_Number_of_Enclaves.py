import collections
from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        cnt = 0
        n = len(A)
        m = len(A[0])

        def bfs(i, j):
            nonlocal cnt
            A[i][j] = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] > 0:
                    bfs(x, y)

        def dfs(i, j):
            q = collections.deque([(i, j)])
            while q:
                i, j = q.popleft()
                if A[i][j] == 0:
                    continue
                A[i][j] = 0
                for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] > 0:
                        q.append((x, y))

        for i in range(n):
            if A[i][0] == 1:
                dfs(i, 0)
            if A[i][m - 1] == 1:
                dfs(i, m - 1)
        for j in range(m):
            if A[0][j] == 1:
                dfs(0, j)
            if A[n - 1][j] == 1:
                dfs(n - 1, j)

        return sum(A[i][j] for j in range(m) for i in range(n))

if __name__ == '__main__':
    s = Solution()
    s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
    #s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])