import collections
import heapq
from typing import List


class SolutionWrong:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # a deque is faster at removing elements from the front

        graph = collections.defaultdict(dict)
        for u, v, dist in edges:
            if dist < distanceThreshold:
                graph[u][v] = dist
                graph[v][u] = dist

        # print(graph)
        def find_dist(start):

            distances = {vertex: float('inf') for vertex in graph}
            pq = []
            pq_update = {}
            distances[start] = 0

            for vertex, value in distances.items():
                entry = [vertex, value]
                heapq.heappush(pq, entry)
                pq_update[vertex] = entry

            while pq:

                getmin = heapq.heappop(pq)[0]

                for neighbour, distance_neigh in graph[getmin].items():
                    dist = distances[getmin] + distance_neigh
                    if dist < distances[neighbour]:
                        distances[neighbour] = dist
                        pq_update[neighbour][1] = dist  # THIS LINE !!!
            # print(distances)
            return distances

        #         def find_dist(start):
        #             destinations = {start:0}
        #             queue = collections.deque([start])

        #             while queue:
        #                 u = queue.popleft()
        #                 dist = destinations[u]
        #                 for v, vdist in graph[u].items():
        #                     vdist+=dist
        #                     if vdist > distanceThreshold:
        #                         continue
        #                     if v not in destinations:
        #                         queue.append(v)
        #                         destinations[v] = vdist
        #                     elif vdist < destinations[v]:
        #                         destinations[v] = vdist
        #             destinations.pop(start)
        #             return destinations
        reachable_cities = float('inf')
        curr_node = -1
        # print(find_dist(1))
        for key in range(n):
            dists = find_dist(key)
            if len(dists) < reachable_cities:
                curr_node = key
                reachable_cities = len(dists)
            elif len(dists) == reachable_cities and curr_node < key:
                curr_node = key
        return curr_node


from heapq import heappush, heappop


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # this for fast taking weight of the edge
        cost = [[float('inf')] * n for _ in range(n)]
        graph = collections.defaultdict(list)
        for a, b, c in edges:
            cost[a][b] = cost[b][a] = c
            graph[a].append(b)
            graph[b].append(a)

        def dijkstra(i):
            dis = [float('inf')] * n
            dis[i], pq = 0, [(0, i)]
            heapq.heapify(pq)
            while pq:
                d, i = heapq.heappop(pq)
                if d > dis[i]: continue
                for j in graph[i]:
                    this_cost = d + cost[i][j]
                    if this_cost < dis[j]:
                        dis[j] = this_cost
                        heapq.heappush(pq, (this_cost, j))
            return sum(d <= distanceThreshold for d in dis) - 1

        res = {dijkstra(i): i for i in range(n)}
        return res[min(res)]

if __name__ == '__main__':
    s = Solution()
    s.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4)

