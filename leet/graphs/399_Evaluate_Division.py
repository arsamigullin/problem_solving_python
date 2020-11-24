import collections
from typing import List


class SolutionMy:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = collections.defaultdict(list)

        for (a, b), k in zip(equations, values):
            d[a].append((b, k))
            d[b].append((a, 1 / k))

        visited = set()

        def dfs(node, target):
            if node not in visited:
                visited.add(node)
                for child, val in d[node]:
                    if child == target:
                        return val
                    if child not in visited:
                        res = dfs(child, target)
                        if res == -1:
                            continue
                        else:
                            return val * res
            return -1

        res = []
        for a, b in queries:
            res.append(dfs(a, b))
            visited = set()

        return res


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = collections.defaultdict(list)
        # let's express divider and dividend
        # divider/dividend = quotient
        # divider = dividend * quotient
        # dividend = divider / quotient
        # thus we build adjacency list where each node contains
        # all possible expressions of the node
        for (dividend, divider), quotient in zip(equations, values):
            d[dividend].append((divider, quotient))
            d[divider].append((dividend, 1 / quotient))
        res = []

        parent = {}
        size = {}

        def find(p):
            parent.setdefault(p, (p, 1))
            root = p
            while root != parent[root][0]:
                root = parent[root][0]
            while p != root:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):

            rootP = find(p)
            rootQ = find(q)

            if size[rootQ] == size[rootP]:
                return

            if size[rootQ] > size[rootP]:
                size[rootQ] += size[rootP]
                parent[rootP] = parent[rootQ]
            else:
                size[rootP] += size[rootQ]
                parent[rootQ] = parent[rootP]
