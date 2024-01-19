from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cantor_pairing_func(x, y):

            x = map_number(x)
            y = map_number(y)
            return 0.5 * (x + y) * (x + y + 1) + y

        def map_number(x):
            return 2 * x if x >= 0 else -2 * x - 1

        # print([cantor_pairing_func(x,y) for x,y in points])

        n = len(points)
        costpoints = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                costpoints.append((cost, cantor_pairing_func(x1, y1), cantor_pairing_func(x2, y2)))

        costpoints.sort()
        # print(costpoints)
        size = {}
        parent = {}

        def find(p):
            parent.setdefault(p, p)
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]

        def union(q, p):
            size.setdefault(q, 1)
            size.setdefault(p, 1)
            parentP = find(p)
            parentQ = find(q)
            if parentP == parentQ:
                return False
            if size[parentP] > size[parentQ]:
                parent[parentQ] = parentP
                size[parentP] += size[parentQ]
            else:
                parent[parentP] = parentQ
                size[parentQ] += size[parentP]
            return True

        result = 0
        n = len(points)
        edge_used = 0
        for cost, p1, p2 in costpoints:
            if union(p1, p2):
                result += cost
                edge_used += 1
                if edge_used == n - 1:
                    break
            # if find(p1)!=find(p2):
            #

        return result


