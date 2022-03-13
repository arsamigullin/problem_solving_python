import collections


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        # 1. Compose graph
        graph = collections.defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        # stores vertices and component number the vertex belongs to
        components = {}

        # 2. Find connected components
        # this function fills components dictionary
        def dfs(node, cmpNum):
            components[node] = cmpNum
            for child in graph[node]:
                if child in components:
                    continue
                dfs(child, cmpNum)

        cmp = 0  # component number
        for node in graph:
            if node not in components:
                dfs(node, cmp)
                cmp += 1

            # 3. Check if two words are in the same component
        for a, b in zip(words1, words2):
            if a == b:
                continue
            # in case of one or two words not in components
            # they will have defferent negative default values so we always return False in this case
            components.setdefault(a, -1)
            components.setdefault(b, -2)
            if components[a] != components[b]:
                return False
        return True