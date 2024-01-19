from collections import defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {ch: set() for ch in ''.join(words)}
        n = len(words)
        for i in range(n - 1):
            first = words[i]
            second = words[i + 1]
            for f, s in zip(first, second):
                if f != s:
                    graph[f].add(s)
                    break
            else:
                if len(first) > len(second):
                    # print("test")
                    return ""

        order = []
        visited = defaultdict(int)

        def topsort(node):
            if visited[node] == 0:
                visited[node] = 1
                for ch in graph[node]:
                    if not topsort(ch):
                        return False
                visited[node] = 2
                order.append(node)
                return True
            else:
                return visited[node] == 2

        for node in graph:
            if visited[node] == 0:
                if not topsort(node):
                    return ""

        return ''.join(reversed(order))
