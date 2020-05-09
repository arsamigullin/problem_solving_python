from typing import List

# union - find
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        countComponent = N
        parent = [i for i in range(N)]
        size = [1 for _ in range(N)]

        def find(p):
            root = p
            while root != parent[root]:
                root = parent[root]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            nonlocal countComponent
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
            countComponent -= 1

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    if i != j and find(i) != find(j):
                        union(i, j)
                    M[j][i] = 0
        return countComponent


class Solution1:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()

        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans

if __name__ == '__main__':
    s= Solution()
    s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])