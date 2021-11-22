import collections
import heapq
import math
from typing import List

# SSSP
# According to Steven Halim, p.196, based on the graph representation the time complexity may be different
# If Adjacency Matrix, then V*V
# If Adjacency List, then V+E
# In Dijkstra's algo we deal with AL, we do enumerate all Vertices and Edges
# O((V+E)lgV)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # classic dijkstra
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        distance = [math.inf] * (n + 1)
        distance[k] = 0
        pq = [(0, k)]
        while pq:
            dis, node = heapq.heappop(pq)
            if dis > distance[node]:
                continue
            for ch, ch_dis in graph[node]:
                if dis + ch_dis < distance[ch]:
                    distance[ch] = dis + ch_dis
                    heapq.heappush(pq, (distance[ch], ch))
        max_val = max(distance[1:])
        return -1 if max_val == math.inf else max_val

class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1

if __name__ == '__main__':
    s = Solution()
    s.networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], 3, 1)