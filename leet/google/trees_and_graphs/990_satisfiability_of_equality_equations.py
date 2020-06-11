
# union-find approach
import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parent = {}
        size = {}
        equations.sort(key=lambda item: item[1:3], reverse=True)

        def find(p):
            parent.setdefault(p, p)
            size.setdefault(p, 1)
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
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = parent[rootP]
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = parent[rootQ]
                size[rootQ] += size[rootP]

        for eq in equations:
            operator = eq[1:3]
            x = eq[:1]
            y = eq[-1:]

            if x in parent and y in parent:
                if operator == '!=':
                    if find(x) == find(y):
                        return False
                else:
                    union(x, y)
            else:
                find(x)
                find(y)
                if operator == '==':
                    union(x, y)
                else:
                    if x == y:
                        return False
        return True

# connected components
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        graph = collections.defaultdict(list)
        for eq in equations:
            op = eq[1:3]
            x = eq[:1]
            y = eq[-1:]
            if op == '!=':
                graph.setdefault(x, [])
                graph.setdefault(y, [])
            else:
                graph[x].append(y)
                graph[y].append(x)

        cmp = 0
        components = {}
        for root in graph:
            if root in components:
                continue
            stack = [root]
            while stack:
                node = stack.pop()
                components[node] = cmp
                for child in graph[node]:
                    if child not in components:
                        stack.append(child)
            cmp += 1

        for eq in equations:
            op = eq[1:3]
            x = eq[:1]
            y = eq[-1:]
            if op == '!=':
                if components[x] == components[y]:
                    return False
            else:
                if components[x] != components[y]:
                    return False

        return True