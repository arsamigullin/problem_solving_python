import collections
from typing import List
# very similar is 785
class Solution:
    '''
    The most important thing about bipartition is
    once the node is colored we can skip it when traversing through the nodes
    in other words we must start only from NOT colored nodes

    let's consider what will happen if we will not do that:
    [[1,3],[0,2],[1,3],[0,2]]

    this graph of this form
    0-------1
    |       |
    |       |
    3-------2
    we will start from 0 and its color is 1
    colors = {0:1}
    we got to three, two and one
    colors = {0:1, 3:0, 2:1, 1:0}

    let's suppose we decided continue with 3
    we want to assign color 1 BUT it has alredy been assigned to color 0
    so we will get wrong result
    we have four nodes here 0,1,2,3

    '''
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        groups = {}

        def dfs(node, group):
            if node not in groups:
                groups[node] = group
                for nei in graph[node]:
                    possible = dfs(nei, group ^ 1)
                    if not possible:
                        return False
                return True
            else:
                return groups[node] == group

        for u in range(1, N + 1):
            if u not in groups:
                if not dfs(u, 0):
                    return False
        return True

class SolutionWrong:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        graph = {}
        for u, v in dislikes:
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, [])
        groups = [N] * (N + 1)
        nocycles = [False] * (N+1)

        def dfs(node, group):
            if nocycles[node]:
                return True
            if groups[node] == N:
                groups[node] = group
                for nei in graph[node]:
                    possible = dfs(nei, group ^ 1)
                    if not possible:
                        return False
                nocycles[node] = True
                return True
            else:
                nocycles[node] = groups[node] == group
                return nocycles[node]

        for u, _ in dislikes:
            if not nocycles[u]:
                groups = [N] * (N + 1)
                if not dfs(u, 0):
                    return False
        return True





if __name__ == '__main__':
    s = Solution()
    s.possibleBipartition(5,
[[1,2],[3,4],[4,5],[3,5]])