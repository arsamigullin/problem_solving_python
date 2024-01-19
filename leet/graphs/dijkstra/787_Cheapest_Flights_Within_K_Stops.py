import math
from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List

# O(N + EKlogEK)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        heap = []

        for s, e, price in flights:
            graph[s].append((e, price))

        heap = [(0, 0, src)]
        dist = [math.inf] * n
        dist[src] = 0
        visited = defaultdict(int)
        while heap:
            node_dist, hops, node = heappop(heap)
            if node == dst:
                if hops <= k + 1:
                    return node_dist
            # instead of looking at the distance we look at the hops
            # if for current node the hops is less that was stored in the visited
            # than we proceed further
            if node not in visited or hops < visited[node]:
                visited[node] = hops
                for ch, ch_dist in graph[node]:
                    heappush(heap, (node_dist + ch_dist, hops + 1, ch))
        return -1

# O(N + EK)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        for s, e, price in flights:
            graph[s].append((e, price))

        q = deque([(0, 0, src)])
        visited = defaultdict(int)
        res = math.inf
        while q:
            dist, hops, node = q.popleft()
            # there is no tracking of visited because it will be cut down by max number of hops which is k
            if hops >= k + 1:
                continue
            # if node == dst:
            # res = min(dist, res)
            # continue
            # visited.add(node)
            for ch, ch_dist in graph[node]:
                # if ch not in visited:
                visited.setdefault(ch, math.inf)
                if dist + ch_dist < visited[ch]:
                    q.append((dist + ch_dist, hops + 1, ch))
                    visited[ch] = dist + ch_dist

        return -1 if visited.setdefault(dst, math.inf) == math.inf else visited[dst]


if __name__ == '__main__':
    s = Solution()
    s.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)