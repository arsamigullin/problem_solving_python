import math
from collections import defaultdict, deque
from typing import List


# O(n⋅m)
from leet.amazon.strings_and_arrays.max_stack import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        dist = [-math.inf] * n
        dist[start_node] = 0
        q = deque([(1, start_node)])

        while q:
            node_prob, node = q.popleft()
            for ch, ch_prob in graph[node]:
                # if ch not in visited:
                # even though it is undirected graph we still do not track visited
                # the reason is even when going from child to parent
                # the probability won't be increase and hence nothing will be added to the q
                if node_prob * ch_prob > dist[ch]:
                    dist[ch] = node_prob * ch_prob
                    q.append((dist[ch], ch))
        # print(dist)
        return 0 if dist[end_node] == -math.inf else dist[end_node]

# Dijkstra O(m+n⋅logn) n eges count, m nodes count
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        dist = [math.inf] * n
        dist[start_node] = 0
        heap = [(-1, start_node)]

        while heap:
            # node_prob is ALWAYS negative
            node_prob, node = heappop(heap)
            if node == end_node:
                return -node_prob
            # this check is because of https://github.com/stevenhalim/cpbook-code/blob/26fb7376417799f8b84b504d46ea7c8c0cf71c29/ch4/sssp/dijkstra.py#L33
            if node_prob > dist[node]: continue
            for ch, ch_prob in graph[node]:
                # ch_prob is ALWAYS positive
                # this is the reason why in the dist array we always have negative elements
                if node_prob * ch_prob < dist[ch]:
                    dist[ch] = node_prob * ch_prob
                    heappush(heap, (dist[ch], ch))

        return 0 if dist[end_node] == math.inf else -dist[end_node]
