import collections
from heapq import heappush, heappop
from typing import List


class Solution(object):
    '''
    Since we
    According to Levin
    An Euler path , in a graph or multigraph, is a walk through the graph
    which uses every edge exactly once. An Euler circuit is an Euler path
    which starts and stops at the same vertex.
    NOTE: but vertices can be revisited but edges visited exactly once

    In our problem, we are asked to construct an itinerary that uses all the flights (edges),
    starting from the airport of "JFK". As one can see, the problem is actually a variant of Eulerian path,
    with a fixed starting point.
    '''
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = []
        # just compose directed graph
        graph = collections.defaultdict(list)
        for origin, dest in tickets:
            graph[origin].append(dest)

        # sort destination cities in revesed order
        for origin in graph:
            graph[origin].sort(reverse=True)

        def dfs(node):
            destList = graph[node]
            while destList:
                next_dest = destList.pop()
                dfs(next_dest)
            res.append(node)

        dfs('JFK')
        return res[::-1]

class Solution1(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)

class SolutionMyWrong:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for fr, to in tickets:
            heappush(graph[fr], to)
        total = []
        print(graph)
        res = []

        def dfs(node):
            nonlocal total
            res.append(node)
            if len(graph[node]) > 0:
                visited = set()
                to_add = []
                while graph[node]:
                    next_airport = heappop(graph[node])
                    if next_airport in visited:
                        to_add.append(next_airport)
                    else:
                        for airport in to_add:
                            heappush(graph[node], airport)
                        dfs(next_airport)
                        visited.add(next_airport)
                        heappush(graph[node], next_airport)
            if len(res) > len(total):
                print(res)
                total = res[:]
            res.pop()

        dfs('JFK')
        return total

if __name__ == '__main__':
    s = Solution()
    s.findItinerary([["JFK","NRT"],["JFK","KUL"],["KUL","JFK"]])
    s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
