from typing import List


class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        parent = [i for i in range(N)]
        size = [1] * N

        def find(p):
            root = p
            while root!=parent[root]:
                root = parent[root]
            while p!=root:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p,q):
            nonlocal N
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP]<size[rootQ]:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            else:
                parent[rootQ] = rootP
                size[rootP]+= size[rootQ]
            N-=1

        logs.sort(key=lambda x: x[0])
        min_time = float('inf')
        for i, (time, u, v) in enumerate(logs):
            if find(u) != find(v):
                min_time = time
                union(u, v)
        return -1 if N > 1 else min_time


class Solution1:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        if len(logs) == 1:
            return logs[0][0]

        trees = [0] * N
        for _, u, v in logs:
            trees[u] = [u, 0]
            trees[v] = [v, 0]

        if any(item == 0 for item in trees):
            return -1

        def find(u):
            parent, _ = trees[u]
            if u != parent:
                trees[u][0] = find(parent)
            return trees[u][0]

        def union(u, v):
            nonlocal N
            parent_u, rank_u = trees[find(u)]
            parent_v, rank_v = trees[find(v)]
            if rank_u > rank_v:
                trees[parent_u][0] = parent_v
            else:
                trees[parent_v][0] = parent_u
                if rank_v == rank_u:
                    trees[parent_v][1] += 1
            N -= 1

        logs.sort(key=lambda x: x[0])
        min_time = float('inf')
        for i, (time, u, v) in enumerate(logs):
            if find(u) != find(v):
                min_time = time
                union(u, v)
        return -1 if N > 1 else min_time

if __name__ == '__main__':
    s = Solution()
    s.earliestAcq([[0,3,4],[2,6,2],[4,4,0],[3,1,2],[1,1,5]],
7)
    s.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]],6)
    s.earliestAcq(
        [[0, 2, 7], [12, 3, 1], [6, 2, 4], [7, 7, 3], [5, 5, 2], [10, 2, 4], [1, 5, 0], [3, 4, 5], [9, 0, 3], [4, 2, 7], [11, 0, 5], [8, 5, 2], [2, 5, 3]],
        8)


