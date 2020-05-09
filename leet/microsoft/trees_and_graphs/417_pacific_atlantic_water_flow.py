import collections
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        res = set()

        def collect(isPacific):
            visited = set()
            if isPacific:
                start, end, start2, end2, step = 0, n, 0, m, 1
            else:
                start, end, start2, end2, step = n - 1, -1, m - 1, -1, -1
            for i in range(start, end, step):
                for j in range(start2, end2, step):
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()

                        if isPacific:
                            if x - 1 < 0 or y - 1 < 0:
                                dp[x][y] = 1
                            if dp[x][y] == 3:
                                res.add((x, y))
                            if dp[x][y] == 0:
                                continue
                        else:
                            if x + 1 == n or y + 1 == m:
                                dp[x][y] |= 2
                            if dp[x][y] == 3:
                                res.add((x, y))
                            if dp[x][y] in (1, 0):
                                continue

                        if (x, y) in visited:
                            continue
                        visited.add((x, y))
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            p, q = x + dx, y + dy
                            if 0 <= p < n and 0 <= q < m:
                                if matrix[x][y] <= matrix[p][q]:
                                    dp[p][q] |= dp[x][y]
                                    queue.append((p, q))

        collect(True)
        collect(False)
        return res

# this approach much fater
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        mem = [[0] * m for _ in range(n)]
        res = []

        def bfs(ocean):
            visited = set()
            q = collections.deque(ocean)
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = dx + i, dy + j
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] >= matrix[i][j] and (x, y) not in visited:
                        mem[x][y] |= mem[i][j]
                        q.append((x, y))

        pacific = []
        atlantic = []
        # gather pacific top and atlantic bottom side
        for i in range(m):
            pacific.append((0, i))
            mem[0][i] = 1
            atlantic.append((n - 1, i))
            mem[n - 1][i] |= 2
        # gather pacific left and atlantic right side
        for j in range(n):
            pacific.append((j, 0))
            mem[j][0] |= 1
            atlantic.append((j, m - 1))
            mem[j][m - 1] |= 2
        # put into the mem
        bfs(pacific)
        bfs(atlantic)

        # we have here separate code to gather res because of this test case
        # [[1,2,2,3,5]]
        for i in range(n):
            for j in range(m):
                if mem[i][j] == 3:
                    res.append((i, j))
        return res


if __name__ == '__main__':
    s = Solution()
    s.pacificAtlantic([[11,2,11,0,15,12,4,15,0,14,11,3,19,11,5,11,18,19,4,3,11,1,9,17,5,2,15,18,11,15],[12,10,8,15,4,7,4,5,7,8,5,12,3,3,10,12,16,15,17,13,13,16,0,0,17,17,11,3,14,0],[8,18,1,6,15,16,14,11,9,11,3,4,17,7,2,16,18,2,0,0,16,18,10,15,14,18,10,19,17,6],[14,17,4,13,13,6,16,1,3,18,18,18,4,1,15,4,0,9,19,3,6,7,19,13,11,11,10,19,3,15],[16,6,19,17,19,17,5,12,6,3,1,0,3,10,13,18,4,3,9,0,1,18,9,15,18,3,4,6,1,15],[1,2,12,9,9,7,17,0,1,14,18,1,5,3,0,7,2,19,7,19,1,11,1,3,2,4,0,3,16,18],[18,10,10,3,12,11,7,8,3,16,7,11,11,12,15,1,13,9,8,17,1,9,7,19,1,14,8,10,18,14],[5,19,9,4,10,14,1,5,11,16,11,3,5,4,19,8,11,16,19,12,6,3,18,16,17,8,11,19,7,14],[0,15,17,11,10,13,19,0,10,3,15,19,3,3,3,4,3,12,17,10,5,16,12,5,5,17,5,17,6,6],[8,19,9,3,13,8,13,17,4,12,13,8,13,12,10,10,16,7,2,8,17,3,7,1,7,16,11,19,13,19],[6,19,6,13,10,5,14,7,3,1,10,6,4,8,15,0,0,2,12,13,14,14,7,5,1,16,15,15,4,7],[7,7,11,14,2,4,14,2,2,0,6,11,15,14,11,13,2,3,14,9,16,3,8,15,2,18,15,15,2,2],[7,5,12,10,14,3,6,9,2,1,2,15,0,4,7,9,7,12,15,9,2,13,7,8,7,9,4,3,5,19],[11,9,1,8,0,15,1,6,5,11,14,19,6,11,0,12,1,6,8,7,0,1,2,9,14,4,5,8,3,16],[8,0,11,5,14,4,19,0,6,8,1,10,13,8,18,6,6,4,5,9,10,14,14,13,12,16,4,3,3,11],[0,9,6,19,16,4,5,10,13,19,8,15,14,7,13,11,17,18,14,18,19,11,0,4,12,11,2,8,17,14],[16,19,16,9,9,14,5,13,7,10,18,6,15,12,12,1,11,16,1,8,1,7,16,7,19,6,12,0,15,0],[2,4,18,15,13,9,4,18,19,5,16,7,10,1,7,7,4,4,10,8,13,15,9,4,16,13,6,3,13,7],[3,11,10,13,6,4,0,13,11,4,5,6,19,13,8,10,8,9,2,4,4,11,12,8,12,15,6,1,10,12],[7,6,19,3,2,14,15,6,9,1,6,14,4,15,13,9,14,7,10,12,17,18,6,4,12,4,1,6,6,12],[15,17,9,15,9,15,9,10,10,11,12,17,2,18,11,0,6,11,14,17,2,13,9,13,3,4,3,1,8,11],[17,13,12,17,4,19,19,7,7,13,19,10,4,16,1,18,14,2,9,18,2,8,3,1,10,9,12,6,2,11],[17,12,6,8,3,16,5,2,16,3,13,3,13,9,11,11,5,12,14,16,3,19,16,16,1,14,5,3,17,19],[1,4,0,3,1,17,5,15,2,19,12,7,18,13,1,0,7,2,9,18,10,18,8,9,13,13,8,10,14,14],[9,14,4,18,10,18,3,9,9,17,16,4,19,7,3,18,7,0,10,13,9,10,11,16,3,5,1,2,16,19],[8,10,13,8,7,2,9,4,16,15,5,4,15,7,9,7,15,2,6,17,14,3,13,3,4,15,13,10,8,16],[17,7,19,19,13,12,6,0,11,4,10,4,1,9,15,9,7,7,14,6,7,18,9,13,6,16,5,2,17,1],[2,7,0,4,8,18,4,11,13,4,11,12,3,18,11,2,4,18,3,3,17,9,18,11,9,15,14,19,7,17],[13,1,15,18,4,12,18,18,15,16,7,17,9,15,11,3,9,7,18,13,3,11,7,19,10,10,7,13,7,19],[17,17,14,3,19,7,1,13,9,3,6,16,10,8,14,8,17,18,12,11,4,11,10,15,9,0,4,12,7,15],[4,4,8,1,7,11,13,4,11,5,18,2,16,11,16,13,0,13,13,12,11,15,8,4,0,3,2,9,8,15],[17,4,13,5,3,17,14,4,7,6,6,11,16,18,2,0,3,12,1,5,12,16,3,14,4,16,5,8,15,9],[5,3,17,17,6,4,19,5,4,6,11,4,14,18,4,19,16,15,1,17,3,8,13,14,16,13,18,19,6,4],[15,0,8,15,6,6,11,8,18,2,4,10,18,16,15,8,1,5,9,13,7,19,12,2,9,18,1,15,12,8],[5,0,18,14,1,8,18,15,5,13,15,7,8,8,9,0,14,12,4,17,2,10,9,7,19,7,19,9,7,1],[7,4,16,16,13,4,3,6,15,11,14,7,3,0,5,15,10,13,18,18,11,6,7,9,19,13,4,2,7,9],[9,14,15,11,14,5,15,1,19,15,3,4,0,10,4,1,2,15,18,15,15,2,9,0,3,10,9,16,4,1],[14,13,17,19,0,13,15,9,16,18,5,6,16,16,6,10,14,15,17,5,9,2,5,11,19,19,11,6,15,14],[17,7,19,6,5,19,10,2,11,17,17,13,16,13,19,4,12,3,4,13,7,9,19,9,12,3,16,8,18,13]])
    s.pacificAtlantic([[10,10,1,11,2,15,17,6,17,10,0,10,18,9,16,13,8,9,12,6,3,2,5,19,4,14],[12,19,13,2,7,2,3,8,17,4,2,1,8,13,7,2,10,16,12,3,4,12,4,16,0,12],[1,12,9,18,12,16,17,5,13,0,7,13,12,13,6,2,11,19,7,2,6,11,11,0,17,6],[1,12,2,0,11,7,7,3,7,13,11,1,11,15,5,13,14,12,4,10,5,16,3,17,18,12],[9,16,11,5,9,13,7,18,18,14,19,10,9,4,8,14,4,19,13,1,14,8,0,3,12,10],[10,19,9,11,1,18,1,2,1,8,1,5,2,15,14,13,18,18,11,4,15,3,15,12,12,2],[0,10,9,2,15,9,12,7,0,0,12,18,9,12,18,4,18,10,3,1,17,14,13,18,9,4],[3,19,9,16,16,19,11,19,6,9,18,0,12,11,13,1,15,6,9,18,9,6,3,12,12,2],[0,16,15,12,3,19,18,9,5,1,4,3,19,15,1,0,7,10,14,4,8,10,15,16,14,8],[15,9,3,15,19,17,17,10,9,8,16,11,3,15,15,9,1,14,11,13,16,7,1,7,13,5],[9,19,6,7,19,14,4,18,6,10,19,13,12,7,7,15,6,10,7,8,8,8,19,13,17,14],[14,7,1,15,2,6,12,4,2,19,17,17,8,9,19,10,0,12,4,12,4,16,15,18,8,0],[4,8,5,8,0,2,19,18,1,7,13,9,13,16,6,15,15,12,18,5,8,11,6,17,5,11],[17,16,9,19,12,6,13,19,0,6,7,9,7,13,9,18,5,15,16,8,18,9,6,0,11,14],[11,5,13,3,12,19,5,15,2,15,9,16,6,12,8,0,19,19,11,0,16,8,15,15,1,12],[15,16,16,19,14,1,2,11,14,8,16,13,2,0,3,8,1,5,4,15,12,5,13,3,5,3]])
    s.pacificAtlantic([[4,4,1,7,4,18,5,5,1,6,6,10,17,19,13,3,19],[19,8,3,14,18,11,2,2,5,2,19,15,18,12,16,7,19],[2,4,15,2,6,4,18,13,12,11,0,11,6,19,17,11,9],[10,2,0,7,13,3,7,0,5,4,10,2,3,18,10,8,10],[13,16,8,5,15,12,8,14,16,18,18,19,10,14,9,4,12],[0,16,14,14,13,15,2,16,1,13,17,9,6,11,17,4,13],[7,9,1,5,18,15,2,1,13,3,0,7,8,8,9,12,0],[7,13,14,5,3,16,5,4,5,3,9,11,11,3,1,17,12],[8,18,17,9,1,0,18,7,16,15,14,14,16,8,11,13,10],[14,19,19,19,19,12,2,17,17,8,10,19,16,7,10,12,17],[7,0,5,2,10,7,1,0,15,3,5,2,14,16,17,9,10],[11,10,15,4,17,11,17,14,18,11,17,15,19,1,9,7,17],[10,8,12,15,13,3,15,14,5,4,4,4,0,11,16,14,15],[16,5,3,5,13,1,6,3,8,9,3,18,11,9,7,5,14],[5,7,14,13,6,12,10,6,6,12,5,0,2,0,0,15,19],[14,11,17,13,6,11,15,0,6,4,5,1,15,1,19,0,14],[17,5,0,0,10,13,4,10,17,5,5,6,16,19,1,11,0],[14,18,11,8,0,1,0,11,1,7,15,11,4,5,18,14,19],[17,10,17,17,1,17,16,16,19,15,0,14,15,2,1,18,4],[12,13,0,15,16,3,1,7,10,9,0,2,13,4,7,1,15],[9,6,17,12,6,19,2,15,3,14,10,15,10,11,15,13,10],[2,19,4,12,19,5,18,9,4,5,1,9,17,8,14,12,15],[5,1,6,17,0,15,13,3,14,13,15,4,15,11,7,15,4],[14,5,6,9,11,6,4,10,16,11,6,6,0,17,13,1,10],[5,18,3,15,10,6,10,6,12,5,13,2,5,7,3,3,19],[11,7,17,17,8,2,11,3,0,7,16,13,7,0,12,11,14],[18,1,19,7,14,9,8,2,3,16,7,9,16,4,18,8,3],[5,8,19,0,10,12,9,12,10,2,11,3,15,8,18,12,3],[15,2,4,9,4,4,18,12,6,10,10,3,6,6,17,3,14],[18,17,13,0,12,15,3,2,15,17,8,16,8,7,17,18,2],[5,12,12,17,18,11,8,6,13,13,14,18,17,9,16,8,5],[16,1,9,13,6,12,15,3,12,6,2,14,10,16,11,3,8],[0,7,16,3,7,0,10,10,7,3,4,18,7,18,7,15,12],[8,7,12,17,8,8,18,11,7,12,18,2,19,6,6,3,13],[6,19,14,9,16,9,13,13,4,11,0,0,3,1,9,10,7],[0,8,14,13,1,7,7,7,2,15,12,6,10,10,3,14,8],[10,17,1,8,8,16,14,18,18,1,10,12,3,13,10,6,5],[8,17,17,6,2,14,5,3,7,5,4,5,13,14,17,14,15],[2,6,12,4,14,11,14,3,12,10,12,15,9,7,0,4,5],[13,11,5,13,12,3,19,10,16,8,3,11,7,10,0,5,18],[0,18,1,8,19,11,0,1,2,19,14,11,10,15,12,3,15]])
    s.pacificAtlantic([[1,2,2],[3,2,3],[2,4,5]])
    s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])