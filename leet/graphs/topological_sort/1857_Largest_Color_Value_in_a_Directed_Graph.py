import collections
from collections import defaultdict, Counter
from functools import lru_cache
from typing import List


class SolutionMy:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        if not edges:
            return 1
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
            indegree.setdefault(u, 0)
        cols = set(colors)
        visited = defaultdict(int)
        result = -1

        def merge(a, b):
            res = Counter()
            for ch in cols:
                res[ch] = max(a[ch], b[ch])
            return res

        @lru_cache(None)
        def topo(node):
            if visited[node] == 0:
                visited[node] = 1
                memo = Counter()
                for ch in graph[node]:
                    isCycle, cache = topo(ch)
                    if not isCycle:
                        return (False, 0)
                    memo = merge(memo, cache)
                memo[colors[node]] += 1
                visited[node] = 2
                return True, memo
            else:
                return (visited[node] == 2, 0)

        # print(indegree)
        # print(graph)
        for node in indegree:
            visited = defaultdict(int)
            if indegree[node] == 0:
                isCycle, memo = topo(node)
                if not isCycle:
                    return -1
                result = max(result, max(memo.values()))
        return result


class SolutionTopoKhanDFS:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        topo_order = []
        queue = collections.deque([i for i, cnt in enumerate(indegree) if cnt == 0])
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
        if len(topo_order) != n:
            return -1
        ans = 0
        for ch in set(colors):
            dp = [0] * n
            for node in topo_order:
                if colors[node] == ch:
                    dp[node] += 1
                for prev in graph[node]:
                    dp[prev] = max(dp[prev], dp[node])
            ans = max(ans, max(dp))
        return ans


if __name__ == '__main__':
    s = SolutionTopoKhanDFS()
    s.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]])
