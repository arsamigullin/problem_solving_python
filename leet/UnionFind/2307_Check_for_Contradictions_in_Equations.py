import collections
from typing import List


class Solution:
    def checkContradictions(self, equations: List[List[str]], vals: List[float]) -> bool:
        parents = collections.defaultdict(str)  # {node: parent}
        values = collections.defaultdict(int)  # {node: value}

        def find(x):
            parents.setdefault(x, x)
            values.setdefault(x, 1)
            if parents[x] != x:
                parents[x], val = find(parents[x])
                values[x] *= val
            return parents[x], values[x]

        def union(x, y, value):
            xx, vx = find(x)
            yy, vy = find(y)
            if xx == yy:
                return abs(vx - vy * value) > 0.00001
            else:
                parents[xx] = yy
                values[xx] *= (value * vy) / vx

            return False

        for (x, y), val in zip(equations, vals):
            if union(x, y, val):
                return True
        return False


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        graph = collections.defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1 / val))

        def dfs(node, running_value, vals):
            if node not in vals:
                vals[node] = running_value
                for ch, val in graph[node]:
                    if ch in vals:
                        return abs(vals[ch] - running_value * val) > 0.00001
                    else:
                        if dfs(ch, running_value * val, vals):
                            return True
            return False

        return any(dfs(node, 1, collections.defaultdict(float)) for node in graph.keys())


if __name__ == '__main__':
    s = Solution()
    s.checkContradictions([["a","b"],["b","c"],["a","c"]], [3,0.5,1.5])