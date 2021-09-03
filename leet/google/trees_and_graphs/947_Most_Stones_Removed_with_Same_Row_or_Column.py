import collections
from typing import List

class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})


class SolutionUF:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        size = {}
        N = len(stones)
        def find(p):
            parent.setdefault(p, p)
            size.setdefault(p, 1)
            root = p
            while root != parent[root]:
                root = parent[root]
            while p != root:
                par = parent[p]
                parent[p] = root
                p = par
            return root

        def union(p, q):
            nonlocal N
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                size[rootP] += size[rootQ]
                parent[rootQ] = rootP
            else:
                size[rootQ] += size[rootP]
                parent[rootP] = rootQ
            N-=1

        for a, b in stones:
            union(a, b + 10 ** 5)
        parents = set()
        for a, b in stones:
            parents.add(find(a))

        print(N, len(parents))
        return len(stones) - len(parents)


class SolutionConnectedComponents:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones:
            return 0
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        for a, b in stones:
            row[a].add((a, b))
            col[b].add((a, b))

        graph = collections.defaultdict(set)
        for a, b in stones:
            graph[(a, b)] = row[a].union(col[b])

        visited = set()

        def dfs(i, j):
            count = 1
            for x, y in graph[(i, j)]:
                if (x, y) not in visited:
                    visited.add((x, y))
                    count += dfs(x, y)
            return count

        res = 0
        for a, b in stones:
            if (a, b) not in visited:
                visited.add((a, b))
                res += dfs(a, b) - 1
        return res


if __name__ == '__main__':
    s = SolutionUF()
    s.removeStones([[1,2],[3,2],[5,6],[7,8]])
    s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
    s.removeStones([[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]])
