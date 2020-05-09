from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

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
            nonlocal n
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
            n -= 1

        for u, v in edges:
            if find(u) == find(v):
                return False
            else:
                union(u, v)

        return n == 1



class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        print(graph)
        visited = set()
        levels = [n] * n

        def dfs(node, level, parent):
            if levels[node] == n:
                levels[node] = level
                expected_level = level + 1
                for child in graph[node]:
                    if child == parent:
                        continue
                    if not dfs(child, level + 1, node):
                        return False
                return True
            else:
                return levels[node] == level

        cnt = 0
        for i in range(n):
            graph.setdefault(i, [])
            if levels[i] == n:
                if cnt > 0:
                    return False
                if not dfs(i, 0, -1):
                    return False
                cnt += 1

        return True
