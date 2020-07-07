from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(node, path):
            if node == len(graph) - 1:
                res.append(path[:])
                return
            for child in graph[node]:
                path.append(child)
                dfs(child, path)
                path.pop()

        dfs(0, [0])
        return res


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph) - 1
        paths = [[0]]
        answer = []
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == dest:
                    answer.append(path + [n])
                else:
                    paths.append(path + [n])
        return answer