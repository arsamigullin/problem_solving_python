import heapq
import collections


def prim(edges, n):
    # n - count vertices
    # edges[i] is of form [u,v,w] where w is weight
    visited = set()
    graph = collections.defaultdict(list)
    heap = []
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])

    def process(u):
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(heap, [w, v])

    tot_cost = 0
    num_taken = 0
    process(1)
    # MST should have n-1 edges where n is count of vertices
    # we can start from any vertex because it will extract the edge with the lowest weight
    while heap and num_taken < n - 1:
        w, v = heapq.heappop(heap)
        if v not in visited:
            tot_cost += w
            num_taken += 1
            process(v)
    print(tot_cost)


class PrimsChecking:
    def mst(self, edges, n):
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited = set()
        heap = []

        def add_vertex(vertex):
            visited.add(vertex)
            for child, weight in graph[vertex]:
                if child not in visited:
                    heapq.heappush(heap, (weight, child))

        add_vertex(1)
        tot_cost = 0
        edge_num_taken = 0
        while heap and edge_num_taken <= n - 1:
            w, node = heapq.heappop(heap)
            if node not in visited:
                edge_num_taken += 1
                tot_cost += w
                add_vertex(node)
        return tot_cost


if __name__ == '__main__':
    pc = PrimsChecking()
    print(pc.mst([[1, 2, 10], [1, 5, 10], [1, 8, 10], [2, 4, 4], [2, 3, 3], [5, 6, 1], [5, 7, 2], [8, 7, 3]], 8))
    print(prim([[1, 2, 10], [1, 5, 10], [1, 8, 10], [2, 4, 4], [2, 3, 3], [5, 6, 1], [5, 7, 2], [8, 7, 3]], 8))
    # prim([[1,2,4],[1,5,5],[1,8,8],[2,4,4],[2,3,3],[5,6,1],[5,7,2],[8,7,3]], 8)
