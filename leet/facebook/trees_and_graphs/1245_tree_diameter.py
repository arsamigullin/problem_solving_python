import collections
import heapq
from typing import List


class Solution1:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        max_len = 0

        def dfs(node):
            nonlocal max_len
            if node in visited:
                return -1
            visited.add(node)
            heap = []
            for child in adj_list[node]:
                if child != node:
                    heapq.heappush(heap, -(dfs(child) + 1))
            first = 0
            if heap:
                first = abs(heapq.heappop(heap))
            second = 0
            if heap:
                second = abs(heapq.heappop(heap))
            max_len = max(max_len, first + second)
            return max(first, second)

        dfs(edges[0][0])
        return max_len


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # build tree
        connected = dict()
        for x, y in edges:
            connected.setdefault(x, set()).add(y)
            connected.setdefault(y, set()).add(x)

        def bfs(node, level=0):
            """Apply (graph) bfs starting at given node by level
            and return last node in search and levels."""
            queue = [node]
            seen = set(queue)
            while queue:
                temp = []
                for x in queue:
                    for y in connected[x]:
                        if y not in seen:
                            temp.append(y)
                            seen.add(y)
                queue = temp
                level += 1
            return x, level - 1

        # two passes
        # 1st pass - find a node on longest path
        # 2nd pass - find length of longest path (i.e. diameter of the tree)
        node = bfs(0)[0]
        return bfs(node)[1]
if __name__ == '__main__':
    s= Solution()
    s.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]])