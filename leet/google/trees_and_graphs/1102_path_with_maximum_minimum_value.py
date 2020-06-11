from typing import List


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        points = [(i, j) for i in range(n) for j in range(m)]
        # print(points)
        parent = [i for i in range(n * m)]
        size = [1 for i in range(n * m)]

        def find(p):
            root = p
            while root != parent[root]:
                root = parent[root]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)

            if rootQ == rootP:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]

        # sort points by the value each point holds
        # this actually insures that when doing union find we will get the shortest path with maximum values
        points.sort(reverse=True, key=lambda point: A[point[0]][point[1]])

        visited = [[False] * m for _ in range(n)]

        for x, y in points:
            visited[x][y] = True
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                i, j = x + dx, y + dy
                if 0 <= i < n and 0 <= j < m and visited[i][j] == True:
                    union(x * m + y, i * m + j)
            if find(0) == find(n * m - 1):
                return A[x][y]
        return -1

# dijkstra
class Solution1:
    def maximumMinimumPath(self, g: List[List[int]]) -> int:
        # it is related to find a path
        # so think as bfs, then how can find the max one
        # use dijkstra
        from heapq import heappush, heappop
        m, n = len(g), len(g[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = []
        heappush(q, (-g[0][0], 0, 0))
        res = g[0][0]
        g[0][0] = -1
        while q:
            nv, i, j = heappop(q)
            res = min(res, -nv)
            if i == m - 1 and j == n - 1:
                return res
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and g[ni][nj] > -1:
                    heappush(q, (-g[ni][nj], ni, nj))
                    g[ni][nj] = -1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maximumMinimumPath([[5, 4, 5], [1, 2, 6], [7, 4, 6]]))
