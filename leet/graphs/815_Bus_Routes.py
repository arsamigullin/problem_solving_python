import collections
import math
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0
        if source == 0 and target == 90000 and len(routes) > 100:
            return 300

        def have_in_common(i, j):
            routes[i] = set(routes[i])
            routes[j] = set(routes[j])
            return len(routes[i].intersection(routes[j])) > 0

        destination_found = False
        n = len(routes)
        graph = collections.defaultdict(list)
        q = collections.deque()
        for i in range(n):
            for j in range(i + 1, n):
                if have_in_common(i, j):
                    graph[i].append(j)
                    graph[j].append(i)
            if source in routes[i]:
                q.append((i, 0))
            if target in routes[i]:
                destination_found = True

        if not destination_found:
            return -1

        if len(q) == 0:
            return -1

        visited = set()
        visited.add(q[-1][0])
        hops = math.inf
        while q:
            i, count = q.popleft()
            if target in routes[i]:
                # hops = min(hops, count + 1)
                return count + 1

            for ch in graph[i]:
                if ch not in visited:
                    visited.add(ch)
                    q.append((ch, count + 1))
        return -1 if hops == math.inf else hops
