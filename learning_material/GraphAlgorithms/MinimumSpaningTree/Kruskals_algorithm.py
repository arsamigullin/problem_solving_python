class Solution:
    def solve(self, N, edges):
        # assuming each item of edge consists of array of len 3
        # where arr[0] - first vertex
        # arr[1] - second vertex
        # arr[2] - weight
        # complexity EOlogV

        parent = [i for i in range(N + 1)]
        size = [1 for _ in range(N + 1)]

        def find(p):
            root = p
            while root != parent[root]:
                root = parent[root]
            while p != root:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            nonlocal N
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            N -= 1

        # sort edges by weight
        edges.sort(key=lambda item: item[2])

        cost = 0
        for u, v, c in edges:
            # if the edge we want to add will not create a cycle
            if find(u) != find(v):
                # add it
                union(u, v)
                cost += c
            else:
                print(u,v)
        return -1 if N != 1 else cost

if __name__ == '__main__':
    s = Solution()
    #print(s.solve(8, [[1, 2, 5],[1, 3, 4],[2, 3, 2],[3, 5, 4],[2, 4, 3],[5, 4, 2],[5, 6, 1],[4, 7, 6],[6, 7, 8],[7, 8, 2]]))
    #print(s.solve(6,[[1,2,4],[1,6,5],[1,4,3],[2,3,3],[2,5,4],[3,4,2],[4,5,3],[5,6,1]]))
    print(s.solve(8,[[1,2,4],[1,5,5],[1,8,8],[2,4,4],[2,3,3],[5,6,1],[5,7,2],[8,7,3]]))