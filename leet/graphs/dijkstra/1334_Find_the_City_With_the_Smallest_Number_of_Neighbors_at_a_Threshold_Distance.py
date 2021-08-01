import collections
import heapq
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = collections.defaultdict(list)
        cost = [[0] * n for _ in range(n)]
        for u, v, w in edges:
            graph[u].append(v)
            graph[v].append(u)
            cost[u][v] = cost[v][u] = w

        found_city = 0
        dist = float('inf')
        for city in range(n):
            distance = [float('inf')] * n
            distance[city] = 0
            h = [(0, city)]
            heapq.heapify(h)
            while h:
                w, i = heapq.heappop(h)
                if w > distance[i]:
                    continue
                for j in graph[i]:
                    this_cost = w + cost[i][j]
                    if this_cost < distance[j]:
                        distance[j] = this_cost
                        heapq.heappush(h, (this_cost, j))
            cnt = sum(d<=distanceThreshold for d in distance) -1
            if cnt <= dist:
                found_city = city
                dist = cnt
        return found_city

if __name__ == '__main__':
    s = Solution()
    s.findTheCity(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4)
