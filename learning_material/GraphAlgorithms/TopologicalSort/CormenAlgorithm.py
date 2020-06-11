import collections
from typing import List


class Solution:
    def solve(self, n, edges: List[List[int]]) -> bool:

        graph = {}
        for u, v in edges:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, [])

        WHITE, GRAY, BLACK = 0, 1, 2
        colors = [0] * n
        order = collections.deque()
        def dfs(node):
            if colors[node] == WHITE:
                colors[node] = GRAY
                for child in graph[node]:
                    if not dfs(child):
                        return False
                colors[node] = BLACK
                order.appendleft(node)
                return True
            else:
                return colors[node] == BLACK

        for u in range(n):
            if not dfs(u):
                return False
        print(order)
        return True


if __name__ == '__main__':
    s = Solution()
    s.solve(6, [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]])
    s.solve(3,
[[0,1],[0,2],[1,2]])

    # g = Graph(6)
    # g.addEdge(5, 2);
    # g.addEdge(5, 0);
    # g.addEdge(4, 0);
    # g.addEdge(4, 1);
    # g.addEdge(2, 3);
    # g.addEdge(3, 1);