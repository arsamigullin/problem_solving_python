import collections
from typing import List

# [["a","b"],["b","c"]]
# [2.0,3.0]
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# we compose graph where vertices are dividend and divider
# and values are expressed divider and dividend, for example
# "a": ("b", 2)
# "b": ("a", 1/2), ("c",3)
# "c": ("b", 1/3)

# now, we need to find a/c
# we just find "a" and iterate over its children. It has only "b" child. We go deeper and iterate
# children of "b" (it has 2 children, "a" is visited), so we return 3 because divider 'c' equals
# to the child 'c' of b
# so "a" = "c" * 3 * 2
# a/c = 6

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = collections.defaultdict(list)

        for (a, b), k in zip(equations, values):
            d[a].append((b, k))
            d[b].append((a, 1 / k))

        def helper(dividend, divider, visited):
            for child, val in d[dividend]:
                if child == divider:
                    return val
                if child not in visited:
                    visited.add(child)
                    divider_val = helper(child, divider, visited)
                    if divider_val == -1:
                        continue
                    return divider_val * val
            return -1

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

if __name__ == '__main__':
    s = SolutionMy()
    s.calcEquation([["a","b"],["b","c"]], [2.0,3.0],  [["a","c"],["b","a"]])


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
