import collections
from typing import List




class Solution1:
    def hasNoCycle(self, edges: List[List[int]], n) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        # compose the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # to store colors for each vertex
        colors = [0] * n

        def dfs(node, parent):
            if colors[node] == WHITE:
                colors[node] = GRAY
                for child in graph[node]:
                    if child == parent:
                        continue
                    # cycle detected
                    if not dfs(child, node):
                        return False
                colors[node] = BLACK
                return True
            else:
                return colors[node] == BLACK

        for i in range(n):
            if colors[i] == WHITE:
                if not dfs(i, -1):
                    return False


class Solution2:
    def hasNoCycle(self, edges: List[List[int]], n) -> bool:
        # compose the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # to store colors for each vertex
        levels = [n] * n

        def dfs(node, level, parent):
            if levels[node] == n:
                levels[node] = level
                for child in graph[node]:
                    # we must skip parent to get false positive result
                    if child == parent:
                        continue
                    # cycle detected
                    if not dfs(child, level + 1, node):
                        return False
                return True
            else:
                return levels[node] == level

        for i in range(n):
            if levels[i] == n:
                if not dfs(i,0,-1):
                    return False


# detecting cycle with Union Find
class Solution:
    '''
    The biggest advantage of that approach is
    also provides the count of connected components
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # each index of parent array represents vertex
        # value is a parent of the ith child
        parent = [i for i in range(n)]
        # this represents the size of tree at ith node
        size = [1 for _ in range(n)]

        def find(p):
            root = p
            # first we want to find the root
            while root != parent[root]:
                root = parent[root]
            # once the root is found we want to update the parent of all the intermediate parents of node
            # doing so we flattening the tree
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root


        def union(p, q):
            nonlocal n
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            # we assign the smallest tree to the larges tree
            # doing so we reduce time for find method when it will update the parent for all intermediate parents
            # we simply will go over less count of nodes
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            n -= 1 # this help to count connected components

        for u, v in edges:
            # if two vertices have the same parent
            # this is going to be a cycle
            if find(u) == find(v):
                return False
            else:
                union(u, v)

        return n == 1

if __name__ == '__main__':
    graph = [[0,1],[1,2],[2,0],[1,3]]
    s = Solution1()
    s.leadsToDestination(graph, 4)
    s2 = Solution2()
    s2.hasNoCycle(graph,4)