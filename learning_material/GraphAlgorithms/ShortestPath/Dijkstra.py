import collections
import heapq
from typing import List

# this one and below looks very similar
# but this is much much faster
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
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


from heapq import heappush, heappop


class Solution1:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis = [[float('inf')] * n for _ in range(n)]
        nei = collections.defaultdict(list)
        for i, j, x in edges:
            dis[i][j] = dis[j][i] = x
            nei[i].append(j)
            nei[j].append(i)
        for i in range(n):
            dis[i][i] = 0

        # Dijkstra
        visited = set()
        for i in range(n):
            pool = [(0, i)]  # pool[j] = x:  d(i,j) = x
            while pool:
                x, j = heappop(pool)  # x = d(i,j)
                if (i, j) not in visited and x <= distanceThreshold:  # early stop, if distance exceeds threshold
                    visited.add((i, j))
                    for k in nei[j]:
                        dis[i][k] = min(dis[i][k], x + dis[j][k])  # dis(i,k) = min(dis(i,k), dis(i,j)+dis(j,k))
                        heappush(pool, (dis[i][k], k))

        cities = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        print(dis)
        return cities[min(cities)]


import heapq

def dijkstra(graph, start):

  distances = {vertex:float('inf') for vertex in graph}
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
        pq_update[neighbour][1] = dist # THIS LINE !!!

  print(distances)
  return distances

def shortest_paths_improved(graph, start):
    """Visit all nodes and calculate the shortest paths to each from start"""
    # a deque is faster at removing elements from the front
    queue = collections.deque([start])
    distances = {start: 0}

    while queue:
        node = queue.popleft()
        dist = distances[node]

        for neighbour, neighbour_dist in graph[node].items():
            neighbour_dist += dist
            if neighbour not in distances:
                queue.append(neighbour)
                distances[neighbour] = neighbour_dist
            elif neighbour_dist < distances[neighbour]:
                distances[neighbour] = neighbour_dist

    return distances


if __name__ == '__main__':

  example_graph = {
      'U': {'V': 2, 'W': 5, 'X': 1},
      'V': {'U': 2, 'X': 2, 'W': 3},
      'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
      'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
      'Y': {'X': 1, 'W': 1, 'Z': 1},
      'Z': {'W': 5, 'Y': 1},
  }
  shortest_paths_improved(example_graph, 'X')

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


class Node:

    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        distance = [[float('inf')] * m for _ in range(n)]

        def dijkstra():
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            heap = []
            heapq.heappush(heap, Node(0, 0, grid[0][0]))
            res = 0
            while heap:
                node = heapq.heappop(heap)
                x = node.x
                y = node.y
                dist = node.dist
                if x == n - 1 and y == m - 1:
                    return max(res, dist)
                res = max(res, dist)
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if 0 <= i < n and 0 <= j < m and grid[i][j] > -1:
                        heapq.heappush(heap, Node(i, j, grid[i][j]))
                        grid[i][j] = -1
            return res

        return dijkstra()





