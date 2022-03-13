import collections
from typing import List
# microsoft
# The network rank of two different cities is defined as the total number of directly connected roads to either city.
# If a road is directly connected to both cities, it is only counted once.
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities
# in other words, find the pair of the nodes such that their maximal network rank is maximal

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                cur = len(graph[i]) + len(graph[j]) - (i in graph[j])
                count = max(count, cur)
        return count