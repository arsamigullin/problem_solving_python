# Khan's algorighm of the topological sort

import heapq
import collections
class SteveHalimKhanAlgo:
    def topsort(self, n, edges):
        in_degree = [0] * n
        graph = collections.defaultdict(list)
        # NOTE: how to compose the DAG not to get "The dictionary has changed its size" error while traversing
        # the graph dict
        for u, v in edges:
            graph[v].append(u)
            graph.setdefault(u, [])
            in_degree[u] += 1

        pq = []
        for i, v in enumerate(in_degree):
            if v == 0:
                heapq.heappush(pq, i)

        cnt = 0
        topord = []
        while pq:
            node = heapq.heappop(pq)
            topord.append(node)
            for ch in graph[node]:
                in_degree[ch] -= 1
                if in_degree[ch] > 0:
                    continue
                heapq.heappush(pq, ch)
            cnt += 1

        return cnt == n

if __name__ == '__main__':
    s = SteveHalimKhanAlgo()
    s.topsort(5, [[1,4],[2,4],[3,1],[3,2]])



