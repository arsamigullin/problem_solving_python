import collections
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        graph = collections.defaultdict(list)
        for i in range(n):
            graph.setdefault(strs[i], [])
            for j in range(i + 1, n):
                not_similar_count = 0
                for k in range(m):
                    if strs[i][k] != strs[j][k]:
                        not_similar_count += 1
                    if not_similar_count > 2:
                        break
                else:
                    graph[strs[i]].append(strs[j])
                    graph[strs[j]].append(strs[i])
        visited = set()

        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)

        count = 0
        for word in strs:
            if word not in visited:
                dfs(word)
                count += 1
        return count