# usually fits for the situation where we must preprocess edges (for example by weight)
# and then build graph on the fly
# if no such actions needed it is better to use connected components algorithm
# to determine if two vertices are at the same component for constant time

# detecting cycle with Union Find
from typing import List

# N + MlgN
# N count of nodes
# M count of union operations Which is N-1
class Solution:
    '''
    The biggest advantage of that approach is
    also provides the count of connected components
    '''
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # each index of parent array represents vertex
        # value is a parent of the ith child
        parent = [i for i in range(n)]
        # this represents the size of tree at ith node
        size = [1 for _ in range(n)]

        # find return parent of the p
        # it also updates the parent for all the intermediate nodes between p and root
        def find(p):
            root = p
            # first we want to find the root
            while root != parent[root]:
                root = parent[root]
            # once the root is found we want to update the parent of all the intermediate parents of node
            # doing so we flattening the tree
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        # union unites two components, represented by edge p and q (p as well as q could also be part of another
        # component). After union, p and q are in the same component.
        def union(p, q):
            nonlocal n
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            # we assign the smallest tree to the larges tree
            # doing so we reduce time for find method when it will update the parent for all intermediate parents
            # we simply will go over less count of nodes
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]
            n -= 1 # this help to count connected components

        for u, v in edges:
            # if two vertices have the same parent
            # this is going to be a cycle
            if find(u) == find(v):
                return False
            else:
                union(u, v)

        return n == 1


class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})