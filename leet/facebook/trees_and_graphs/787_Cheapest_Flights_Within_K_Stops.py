import collections
from heapq import heappush, heappop
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cost = [[float('inf')] * n for i in range(n)]
        graph = collections.defaultdict(list)
        for u, v, c in flights:
            graph[v].append(u)
            graph[u].append(v)
            cost[u][v] = cost[v][u] = c
        # dijkstra
        dis = [float('inf')] * n
        dis[src] = 0
        pq = [(0, src, K)]
        min_cost = float('inf')
        while pq:
            d, node, stop = heappop(pq)
            if stop < -1:
                continue
            if node == dst:
                min_cost = min(min_cost, d, dis[node])
            if d > dis[node]:
                continue
            for child in graph[node]:
                cost_to_the_child = d + cost[node][child]
                if cost_to_the_child < dis[child]:
                    heappush(pq, (cost_to_the_child, child, stop - 1))
        return min_cost

if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(5,[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],2,1,1)
    s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)
