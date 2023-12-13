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
            # say we have a/b=9.44
            # parent
            return parents[x], values[x]

        def union(x, y, value):
            xx, vx = find(x)
            yy, vy = find(y)
            if xx == yy:
                return abs(vx - vy * value) > 0.00001
            else:
                parents[xx] = yy
                values[xx] = (value * vy) / vx

            return False

        for (x, y), val in zip(equations, vals):
            if union(x, y, val):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.checkContradictions([["a","b"],["a","c"],["d","b"],["c","f"],["d","b"],["f","f"]], [9.44,4.25,8.63,6.07,8.63,1])