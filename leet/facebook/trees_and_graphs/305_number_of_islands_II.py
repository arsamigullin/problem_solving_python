from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [i for i in range(m * n)]
        size = [1 for i in range(m * n)]
        islands = 0
        res = []

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
            nonlocal islands
            rootP = find(p)
            rootQ = find(q)

            if rootP == rootQ:
                return False

            if size[rootP] > size[rootQ]:
                parent[rootQ] = parent[rootP]
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = parent[rootQ]
                size[rootQ] += size[rootP]
            return True

        water = [[0] * n for _ in range(m)]
        print(water)
        for x, y in positions:

            allzeros = True
            cnt = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and water[i][j] == 1:
                    allzeros = False
                    if find(x*n+y) != find(i * n + j):
                        if cnt > 0:
                            islands -= 1
                    cnt+=1
                    union(x * n + y, i * n + j)
            if allzeros and water[x][y] == 0:
                islands += 1
            res.append(islands)
            water[x][y] = 1
        return res


if __name__ == '__main__':
    s = Solution()
    s.numIslands2(
3,
3,
[[0,0],[0,1],[1,2],[1,2]])
    s.numIslands2(3,
3,
[[0,0],[0,1],[1,2],[2,1],[1,0],[0,0],[2,2],[1,2],[1,1],[0,1]])
    s.numIslands2(3,
3,
[[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]])