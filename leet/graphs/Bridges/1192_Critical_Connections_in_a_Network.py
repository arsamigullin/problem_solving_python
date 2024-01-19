import collections
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        dfs_low = [0] * n
        dfs_num = [0] * n
        iteration_num = 1
        res = []

        def critical_connection(node, parent):
            nonlocal iteration_num

            dfs_low[node] = dfs_num[node] = iteration_num
            iteration_num += 1

            for child in graph[node]:
                if dfs_low[child] == 0:
                    critical_connection(child, node)
                    if dfs_low[child] > dfs_num[node]:
                        res.append((node, child))
                    dfs_low[node] = min(dfs_low[node], dfs_low[child])
                elif child != parent:
                    dfs_low[node] = min(dfs_low[node], dfs_low[child])

        for node in range(n):
            if dfs_low[node] == 0:
                critical_connection(node, -1)

        return res


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        levels = [n] * n
        critical = []

        def dfs(node, level, parent):
            if levels[node] == n:
                levels[node] = level
                expected_child_level = level + 1

                for child in graph[node]:
                    if child != parent:
                        actual_child_level = dfs(child, expected_child_level, node)
                        if actual_child_level == expected_child_level:
                            critical.append([node, child])
                        levels[node] = min(levels[node], actual_child_level)
            return levels[node]

        dfs(0, 0, -1)
        return critical


