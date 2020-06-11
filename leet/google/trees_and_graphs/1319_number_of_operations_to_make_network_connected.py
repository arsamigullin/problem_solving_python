import collections
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        parent = {}
        size = {}

        def find(p):
            parent.setdefault(p, p)
            size.setdefault(p, 1)
            root = p
            while root != parent[root]:
                root = parent[root]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return False
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            return True

        free_cables = 0
        busy_cables = 0
        for u, v in connections:
            if union(u, v):
                busy_cables += 1
            else:
                free_cables += 1

        return n - 1 - busy_cables if busy_cables + free_cables >= n - 1 else -1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        This problem can be solved using connected components


        '''
        # note, if we have less that n-1 connections
        # that means no free cables available

        if (len(connections) < n - 1): return -1
        graph = collections.defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        # here we find connected components
        #
        def dfs(node, visited):

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        count = 0
        visited = set()
        for node in range(n):
            # each unconnnected node is a separate component
            if node not in visited:
                dfs(node, visited)
                count += 1

        return count - 1