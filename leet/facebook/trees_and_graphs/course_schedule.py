#https://leetcode.com/problems/course-schedule/submissions/

# to solve this we use DFS
# The problem boils down to find the cycles in graph
# Algo
# 1. build a graph
# Note: all the nodes are in numCourses range
# 2. We also maintain states
# 3. Each vertes has three states:
    # 0 - unvisited
    # 1 - visiting
    # 2 - visited
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = [[] for _ in range(numCourses)]
        states = [0] * numCourses
        def dfs(vertex):
            states[vertex] = 1
            for child in graph[vertex] :
                # if the child vertex is in visiting state
                # or maybe one of its children in visiting state
                # we caught a cycle
                if states[child] == 1 or states[child] == 0 and not dfs(child):
                    return False
            states[vertex] = 2
            return True
        # build graph
        for edge in prerequisites:
            u, v = edge
            graph[v].append(u)

        for n in range(numCourses):
            # no need to visit visited nodes again. Only unvisited
            if states[n] == 0:
                if not dfs(n):
                    return False
        return True
if __name__ == "__main__":
    s = Solution()
    s.canFinish(2,[[1,0]])
