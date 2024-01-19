from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph = defaultdict(list)
        con = set()
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
            con.add((u, v))

        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        count = 0
        while q:
            node = q.popleft()
            for ch in graph[node]:
                if ch not in visited:
                    visited.add(ch)
                    q.append(ch)
                    if (node, ch) in con:
                        count += 1

        return count