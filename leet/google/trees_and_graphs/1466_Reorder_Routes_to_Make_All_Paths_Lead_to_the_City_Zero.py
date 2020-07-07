import collections

from leet.microsoft.trees_and_graphs.n_ary_tree_level_order_traversal import List


class SolutionMy:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        directedGraph = collections.defaultdict(set)
        # we compose directed and udirected graphs
        for u, v in connections:
            graph[v].append(u)
            graph[u].append(v)
            directedGraph[u].add(v)

        total = 0
        # we do dfs and then reaching the end of the tree we get we check
        # if parent node is in children of child node
        def dfs(node, parent):
            nonlocal total
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
            if parent != -1 and parent not in directedGraph[node]:
                total += 1

        dfs(0, -1)
        return total

