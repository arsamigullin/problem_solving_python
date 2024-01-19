import collections
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        vs = defaultdict(list)
        for i, u in enumerate(manager):
            vs[u].append(i)

        print(vs)

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
#    4
#    10
#    3
#    9
#  1 6 8  (213,975,261)
#  7 2 5  (0,  0,  170)
#      0

# to notify employee 0 we need 261 + 170 = 431 time
# however manager 6 needs more time to notify employee 2
# so, 431 falls withing 975 and not to count 431 we just pick up 975

        def recursive(u):
            result = 0
            for v in vs[u]:
                result = max(result, recursive(v))
            print(u, result + informTime[u])
            return result + informTime[u]

        return recursive(headID)

if __name__ == '__main__':
    s = Solution()
    s.numOfMinutes(11,4,[5,9,6,10,-1,8,9,1,9,3,4],[0,213,0,253,686,170,975,0,261,309,337])


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = collections.defaultdict(list)
        headIdTime = 0
        for i in range(n):
            if manager[i] == -1:
                headIdTime = informTime[i]
                continue
            employee = i
            manag = manager[i]
            graph[manag].append(employee)

        # employee, time
        q = collections.deque([(headID, 0)])
        tot = 0
        while q:
            node, time = q.popleft()
            tot = max(tot, time + informTime[node])
            for ch in graph[node]:
                q.append((ch, time + informTime[node]))
        return tot