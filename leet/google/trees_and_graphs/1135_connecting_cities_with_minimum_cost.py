import collections
from typing import List

# this is the best version
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        parent = [i for i in range(N + 1)]
        size = [1 for _ in range(N + 1)]

        def find(p):
            root = p
            while root != parent[root]:
                root = parent[root]
            while p != root:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            nonlocal N
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            N -= 1

        connections.sort(key=lambda item: item[2])

        cost = 0
        for u, v, c in connections:
            if find(u) != find(v):
                union(u, v)
                cost += c
        return -1 if N != 1 else cost


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        mset = [0] * (N + 1)
        for u, v, _ in connections:
            mset[u] = [u, 0]
            mset[v] = [v, 0]

        def find(v):
            parent, _ = mset[v]
            if v != parent:
                mset[v][0] = find(parent)
            return parent

        def union(u, v):
            pu, urank = mset[find(u)]
            pv, vrank = mset[find(v)]
            if urank > vrank:
                mset[pv][0] = pu
            else:
                mset[pu][0] = pv
                if urank == vrank:
                    mset[pv][1] += 1

        connections.sort(key=lambda item: item[2])

        A = set()
        cost = 0
        for u, v, c in connections:
            if find(u) != find(v):
                A.add((u, v))
                union(u, v)
                cost += c
        return cost


class Solution1:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:

        adj_list = collections.defaultdict(list)
        for u, v, _ in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        if len(adj_list) != N:
            return -1
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        cnt = 2
        for k in adj_list:
            if k not in visited:
                cnt -= 1
                if cnt == 0:
                    return -1
                dfs(k)

        mset = [0] * (N + 1)
        for u, v, _ in connections:
            mset[u] = [u, 0]
            mset[v] = [v, 0]

        def find(v):
            parent, _ = mset[v]
            if v != parent:
                mset[v][0] = find(parent)
            return mset[v][0]

        def union(u, v):
            pu, urank = mset[find(u)]
            pv, vrank = mset[find(v)]
            if urank > vrank:
                mset[pv][0] = pu
            else:
                mset[pu][0] = pv
                if urank == vrank:
                    mset[pv][1] += 1

        connections.sort(key=lambda item: item[2])

        A = set()
        cost = 0
        for u, v, c in connections:
            if find(u) != find(v):
                A.add((u, v, c))
                union(u, v)
                cost += c
        return cost


if __name__ == '__main__':
    s = Solution()
    #s.minimumCost(4, [[1,2,3],[3,4,4]])
    s.minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]])