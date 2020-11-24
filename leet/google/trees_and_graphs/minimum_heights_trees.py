#https://leetcode.com/problems/minimum-height-trees/
# the key things
# we have graph with tree characteristics. this means it will have leaves, i.e. it will not have cycle
# Idea
# the idea behind is to tear leaves gradually approaching to the middle

import collections
import typing
List = typing.List
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        # first we compose the graph
        graph = collections.defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            # and count neighboring nodes for each node
            degree[a] += 1
            degree[b] += 1
        # nodes with neighbor count == 1 are leaves
        queue = [ n for n in range(n) if degree[n]==1 ]
        while queue:
            tmp = []
            ans = queue
            # we tear each leaf
            for leaf in queue:
                for nei in graph[leaf]:
                    # by decreasing count of its parent
                    degree[nei] -= 1
                    # once parent node has count presence 1, it turns to be leaf
                    if degree[nei] == 1:
                        tmp.append(nei)
            queue = tmp
        return ans

    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [x for x in range(n) if len(graph[x]) <= 1]
        prev_leaves = leaves
        while leaves:
            new_leaves = []
            for leaf in leaves:
                # this means leaves are only the items left in graph
                if not graph[leaf]:
                    return leaves
                # remove parent from leaf neighbor
                # here we do pop because leaf has only one parent
                neighbor = graph[leaf].pop()
                # remove leaf from parent neighbor
                graph[neighbor].remove(leaf)
                # once parent has only one connection
                # it becomes leaf
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            # at this moment we got new list of leaves
            # we will take care of it the next loop
            prev_leaves, leaves = leaves, new_leaves

        return prev_leaves

    def findMinHeightTrees3(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = [node for node in range(n) if len(graph[node]) <= 1]
        prev_leaves = []
        while leaves:
            new_leaves = []
            for leaf in leaves:
                if not graph[leaf]:
                    return leaves
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)
            prev_leaves, leaves = leaves, new_leaves

        return prev_leaves


if __name__ == "__main__":
    s= Solution()
    s.findMinHeightTrees2(4, [[1,0],[1,2],[1,3]])
    s.findMinHeightTrees(1,[])
    s.findMinHeightTrees2(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])