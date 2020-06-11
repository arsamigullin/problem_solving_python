# https://leetcode.com/problems/find-the-town-judge/
# Treat the input as matrix-adjacency representation
# you will notice that under the judge column there will be all ones except judge itself
# example [[1,3],[2,3]]
#
#  1  2  3
#1 0  0  1
#2 0  0  1
#3 0  0  0
# i.e. the sum of these ones is equal N-1
import collections
from typing import List


class Solution:
    def findJudge(self, N: int, trust) -> int:
        # if the trust is empty return 1 (since judge does not trust anybody)
        if len(trust) == 0:
            return 1
        judges = [0]*(N+1)
        current = 0
        index = 0
        for i in range(len(trust)):
            a, b = trust[i]
            judges[a]-=1
            judges[b]+=1
            if judges[b] > current:
                current = judges[b]
                index = b
        return index if judges[index] == N-1 else - 1

# treat it as directed graph
# judge must have in_degree == 0
# must have children count N - 1 (i.e. except itself)
# must be the only node with in_degree == 0 (that is because we constructed inversed graph)
# i.e. if 3 is jugdge and 1 trusts 3, the edge will be 3->1 rather than 1->3

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = set([i for i in range(1, N + 1)])
        graph = collections.defaultdict(list)
        for u, v in trust:
            graph[v].append(u)
            in_degree.discard(u)
        if len(in_degree)!=1:
            return -1
        judge = in_degree.pop()
        return judge if len(graph[judge]) == N - 1 else -1