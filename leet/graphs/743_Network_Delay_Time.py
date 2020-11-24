# Dijkstra
# SSSP

from heapq import heappush, heappop
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        INF = int(1e9)
        dist = [INF for u in range(N + 1)]
        dist[K] = 0
        pq = []
        heappush(pq, (0, K))

        AL = [[] for u in range(N + 1)]
        for u, v, w in times:
            AL[u].append((v, w))

            # sort the pairs by non-decreasing distance from s
        while (len(pq) > 0):  # main loop
            d, u = heappop(pq)  # shortest unvisited u
            if (d > dist[u]): continue  # a very important check meaning not need to modify if the distance is greater
            # than
            for v, w in AL[u]:  # all edges from u
                if (dist[u] + w >= dist[v]): continue  # not improving, skip
                dist[v] = dist[u] + w  # relax operation
                heappush(pq, (dist[v], v))

        ans = max(dist[1:])
        return -1 if INF == ans else ans