import collections
from typing import List


class SolutionMy:
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
            while root != p:
                temp = parent[p]
                parent[p] = root
                p = temp
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
            N -= 1

        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)

        for x, y in stones:
            rows[x].append((x, y))
            cols[y].append((x, y))

        for xk in rows:
            for i in range(len(rows[xk]) - 1):
                union(rows[xk][i], rows[xk][i + 1])
            for row in rows[xk]:
                for col in cols[row[1]]:
                    if col == row:
                        continue
                    union(row, col)

        return len(stones) - N



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


class Solution:
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
            while root != p:
                temp = parent[p]
                parent[p] = root
                p = temp
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
            N -= 1

        for x, y in stones:
            union(x, y + 10000)

        print(N)
        r = set()
        for x, y in stones:
            r.add(find(x))
            r.add(find(y + 10000))
        print(len(stones))
        print(r)
        print(parent)
        return len(stones) - len(set(parent.values()))

if __name__ == '__main__':
    s = Solution2()
    s.removeStones([[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]])
    s.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])