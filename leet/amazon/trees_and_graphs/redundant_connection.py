# This problem
# https://leetcode.com/problems/redundant-connection/
import  typing
List = typing.List
class SolutionMy:
    # The idea is to find the cycle in graph
    # and once we found the cycle we go back comparing the edge index
    # we go back and find the edge with highest index in d
    # since to break a cycle we can remove any edge
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        d = {(u, v): i for i, (u, v) in enumerate(edges)}
        # print(d)

        graph = [[] for _ in range(len(edges) + 1)]
        states = [0] * (len(edges) + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)
        res = None
        cycle_starts_at = None

        def dfs(i, parent):
            # print(i, parent)
            nonlocal res
            nonlocal cycle_starts_at

            if i >= len(graph):
                return False
            if states[i] == 1:
                states[i] = 4
                cycle_starts_at = i
                return True
            states[i] = 1
            for child in graph[i]:
                if child == parent:
                    continue
                # print(child, i)
                is_cycle_found = dfs(child, i)
                if is_cycle_found:
                    if not res or (
                            d[(min(child, i), max(child, i))] > d[(res[0], res[1])] and states[cycle_starts_at] == 4):
                        res = (min(child, i), max(child, i))
                    if i == cycle_starts_at:
                        states[cycle_starts_at] = 5
                    return True
            states[i] = 2
            return False

        dfs(1, -1)
        return res

# the approach of finding cycle is the same as in
# critical_connections_in_a_network.py
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        d = {(u,v):i for i, (u,v) in enumerate(edges)}
        # since in this problem the min vertes is 1 (not 0), in range we do +1
        graph = [[]  for _ in range(len(edges)+1)]
        # so, in graph we alway will have graph[0] to be []
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        levels = [len(graph)] * len(graph)
        res = None
        def dfs(node, level, parent):
            nonlocal res
            if levels[node] == len(graph):
                levels[node] = level
                expected_lvl = level + 1
                for nei in graph[node]:
                    if nei == parent:
                        continue
                    actual_lvl = dfs(nei, level+1, node)
                    if expected_lvl!=actual_lvl:
                        if not res or d[(min(nei,node), max(nei, node))] > d[(res[0], res[1])]:
                            res = (min(nei,node), max(nei, node))
                    levels[node] = min(levels[node], actual_lvl)
            return levels[node]
        dfs(1,1,-1)
        return res

if __name__ == '__main__':
    s = Solution()
    s.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])


