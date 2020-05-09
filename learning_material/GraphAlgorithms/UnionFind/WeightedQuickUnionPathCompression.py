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