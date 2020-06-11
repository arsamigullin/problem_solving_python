import collections
import heapq
from typing import List

if __name__ == '__main__':


    n = 5
    source = 0
    edges = [[0,1,10],[0,2,5],[1,2,2],[2,1,3],[1,3,1],[2,4,2],[2,3,9],[4,0,7],[3,4,4],[4,3,6]]

    graph = collections.defaultdict(list)

    for u, v, cost in edges:
        graph[u].append([v, cost])

    n = 5
    source = 0
    edges = [[0, 1, 10], [0, 2, 5], [1, 2, 2], [2, 1, 3], [1, 3, 1], [2, 4, 2], [2, 3, 9], [4, 0, 7], [3, 4, 4],
             [4, 3, 6]]

    graph = collections.defaultdict(list)

    for u, v, cost in edges:
        graph[u].append([v, cost])

    res = [0] * n
    q = [(0, 0)]
    weights = [[float('inf'), i] for i in range(n)]
    weights[0][0] = 0
    q = [weights[0]]
    def relax(u, v, weight):
        du = weights[u][0]
        dv = weights[v][0]
        if dv > du + weight:
            weights[v][0] = du + weight
            return True
        return False

    while q:
        print(q)
        val, u = heapq.heappop(q)
        for v, cost in graph[u]:
            if relax(u,v,cost):
                heapq.heappush(q, weights[v])

    print(weights)
    print('Done')



class Solution:
    def maximumMinimumPath(self, g: List[List[int]]) -> int:
        # it is related to find a path
        # so think as bfs, then how can find the max one
        # use dijkstra
        from heapq import heappush, heappop
        m, n = len(g), len(g[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = []
        heappush(q, (-g[0][0], 0, 0))
        res = g[0][0]
        g[0][0] = -1
        while q:
            nv, i, j = heappop(q)
            res = min(res, -nv)
            if i == m - 1 and j == n - 1:
                return res
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and g[ni][nj] > -1:
                    heappush(q, (-g[ni][nj], ni, nj))
                    g[ni][nj] = -1
        return res

