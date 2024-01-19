import collections
from collections import deque, defaultdict
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        print('order', group)
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for item in range(n):
            indegree.setdefault(item, 0)
            for bitem in beforeItems[item]:
                graph[bitem].append(item)
                indegree[item] += 1
            graph.setdefault(item, [])

        order = []
        groupDict = defaultdict(list)
        groupNum = m
        for item, g in enumerate(group):
            if g == -1:
                groupDict[groupNum].append(item)
                group[item] = groupNum
                groupNum += 1
            else:
                groupDict[g].append(item)

        print(groupDict)

        graphs = defaultdict(dict)
        indegrees = defaultdict(dict)
        visited = set()
        for g in range(groupNum):
            # compose graph and indegree
            for item in groupDict[g]:
                indegrees[g].setdefault(item, 0)
                graphs[g].setdefault(item, [])
                for bitem in beforeItems[item]:
                    bitemGroup = group[bitem]
                    graphs[bitemGroup].setdefault(bitem, [])
                    graphs[bitemGroup].setdefault(item, [])
                    graphs[bitemGroup][bitem].append(item)
                    # indegrees[g].setdefault(bitem, 0)
                    indegrees[bitemGroup].setdefault(item, 0)
                    indegrees[bitemGroup][item] += 1

            print(graphs[g], g)

        print(graphs)
        print(indegrees)

        for g in group:
            graph = graphs[g]
            indegree = indegrees[g]
            print('group', g)
            print(graph)
            print(indegree)
            # populate q
            q = deque()
            for item in graph:
                if item not in indegree:
                    return []
                if indegree[item] == 0:
                    q.append(item)

            curorder = []
            while q:
                node = q.popleft()
                if node not in visited:
                    visited.add(node)
                    order.append(node)
                curorder.append(node)
                for ch in (graph[node]):
                    # if ch not in visited:
                    indegree[ch] -= 1
                    if indegree[ch] == 0:
                        q.append(ch)
            print(curorder, len(graph), groupDict[g], len(curorder))
            if len(curorder) != len(graph):
                return []
                # break

        return order  # [5, 2, 6, 1, 3, 4, 0, 7]


if __name__ == '__main__':
    s = Solution()
    s.sortItems(5,3,[0,0,2,1,0],[[3],[],[],[],[1,3,2]])
    s.sortItems(4,1,[-1,0,0,-1],[[],[0],[1,3],[2]])