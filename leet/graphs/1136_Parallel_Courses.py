import collections
from typing import List

# this is topological sort problem but with slightly modification

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:

        # this is quite traditional beginning for the topological sort
        in_degree = [0] * (n + 1)
        graph = collections.defaultdict(list)
        for u, v in relations:
            graph[u].append(v)
            in_degree[v] += 1

        q = collections.deque()

        # the key point is to start from the nodes that does not have input edges
        for i in range(1, len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        learned_cources = 0
        semesters = 0
        while q:
            # this cycle reflects semester
            semesters += 1
            next_queue = []
            # this cycle reflects study process
            for course in q:
                learned_cources += 1
                end_nodes = graph[course]
                # we just need to understand
                for e in end_nodes:
                    in_degree[e] -= 1
                    # which courses are already learned
                    if in_degree[e] == 0:
                        # so the next semester we will start with these courses
                        next_queue.append(e)
            q = next_queue

        # to ensure there is no cycle, the learned courses should be equal n

        return semesters if learned_cources == n else -1
