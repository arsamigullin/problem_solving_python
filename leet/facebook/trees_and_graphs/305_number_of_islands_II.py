import collections
from typing import List


class Solution1:
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

# clean code
class Solution:
    def numIslands2(self, n: int, m: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        size = {}

        def find(p):
            size.setdefault(p, 1)
            parent.setdefault(p, p)
            rootP = p
            while rootP != parent[rootP]:
                rootP = parent[rootP]
            while p != rootP:
                next_p = parent[p]
                parent[p] = rootP
                p = next_p
            return rootP

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)

            if rootP == rootQ:
                return

            if size[rootP] > size[rootQ]:
                size[rootP] += size[rootQ]
                parent[rootQ] = parent[rootP]
            else:
                size[rootQ] += size[rootP]
                parent[rootP] = parent[rootQ]

        grid = collections.defaultdict(int)
        ISLAND = 1
        island_count = 0
        res = []
        for i, j in positions:
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < n and 0 <= y < m and grid[(x, y)] == ISLAND:
                    # if two cells have different parent that means the count of island should be decreased
                    if find(y + (x * m)) != find(j + (i * m)):
                        union(y + (x * m), j + (i * m))
                        island_count -= 1
            if grid[(i, j)] != ISLAND:
                grid[(i, j)] = ISLAND
                island_count += 1
            res.append(island_count)
        return res

# the same as above but
class Solution:
    def numIslands2(self, n: int, m: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        size = {}

        def find(p):
            size.setdefault(p, 1)
            parent.setdefault(p, p)
            rootP = p
            while rootP != parent[rootP]:
                rootP = parent[rootP]
            while p != rootP:
                next_p = parent[p]
                parent[p] = rootP
                p = next_p
            return rootP

        def union(p, q, count):
            rootP = find(p)
            rootQ = find(q)

            if rootP == rootQ:
                return count

            if size[rootP] > size[rootQ]:
                size[rootP] += size[rootQ]
                parent[rootQ] = parent[rootP]
            else:
                size[rootQ] += size[rootP]
                parent[rootP] = parent[rootQ]
            return count - 1

        grid = collections.defaultdict(int)
        ISLAND = 1
        island_count = 0
        res = []
        for i, j in positions:
            if grid[(i, j)] != ISLAND:
                grid[(i, j)] = ISLAND
                island_count += 1
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < n and 0 <= y < m and grid[(x, y)] == ISLAND:
                    # if two cells have different parent that means the count of island should be decreased
                    island_count = union(y + (x * m), j + (i * m), island_count)
            res.append(island_count)
        return res

if __name__ == '__main__':
    s = Solution()
    s.numIslands2(21,71,
[[19,28],[14,38],[15,44],[17,12],[6,19],[11,69],[2,30],[7,43],[19,6],[7,29],[10,21],[17,55],[20,66],[12,28],[11,64],[12,52],[18,15],[2,52],[10,20],[0,50],[16,5],[17,25],[12,67],[6,45],[13,17],[5,55],[10,42],[20,17],[3,26],[20,61],[14,10],[9,1],[9,69],[6,29],[11,53],[3,66],[4,45],[12,65],[11,35],[5,67],[18,35],[2,57],[12,12],[13,53],[9,65],[13,0],[3,18],[13,39],[5,54],[20,43],[19,29],[17,37],[17,45],[3,38],[2,61],[2,65],[3,21],[5,40],[10,4],[12,36],[2,8],[3,33],[15,4],[13,35],[0,45],[20,29],[10,66],[19,7],[0,46],[19,11],[10,22],[19,0],[0,9],[2,20],[16,64],[10,37],[16,49],[4,20],[20,68],[10,38],[17,59],[15,54],[17,60],[19,18],[0,60],[9,62],[3,69],[10,44],[15,2],[14,44],[17,0],[18,42],[17,28],[11,10],[11,42],[11,67],[0,32],[8,0],[17,6],[7,26],[17,65],[17,66],[7,38],[8,17],[7,60],[0,16],[7,59],[18,8],[16,63],[7,0],[11,46],[0,7],[6,4],[2,63],[8,56],[18,18],[12,70],[2,15],[14,65],[13,52],[11,0],[10,48],[7,8],[11,44],[0,35],[4,64],[6,36],[16,17],[7,34],[1,33],[11,60],[17,11],[4,58],[4,9],[18,7],[15,40],[11,24],[17,3],[7,9],[1,38],[1,14],[15,21],[14,68],[14,69],[16,40],[5,60],[18,46],[15,51],[7,65],[1,34],[15,55],[19,63],[5,35],[20,9],[13,1],[20,69],[19,67],[17,44],[12,44],[10,49],[12,43],[14,21],[18,11],[11,9],[4,56],[6,70],[8,54],[1,55],[17,47],[18,38],[3,31],[16,37],[13,7],[15,6],[18,33],[4,60],[17,40],[7,3],[3,32],[13,41],[5,62],[17,4],[20,5],[15,32],[19,31],[8,69],[19,58],[3,35],[6,64],[0,37],[15,56],[6,46],[4,42],[4,51],[2,7],[7,13],[20,47],[10,29],[12,18],[20,52],[5,5],[12,34],[1,57],[7,32],[3,58],[14,29],[2,32],[2,46],[14,5],[3,9],[19,68],[18,16],[19,2],[6,23],[20,3],[10,69],[9,0],[0,13],[20,38],[6,14],[0,21],[6,50],[2,5],[1,20],[5,20],[1,5],[10,0],[7,6],[15,13],[8,21],[7,14],[9,9],[19,8],[13,25],[5,30],[1,16],[18,19],[16,44],[4,5],[15,37],[20,14],[20,8],[5,23],[13,44],[17,56],[13,62],[2,18],[1,58],[17,2],[20,40],[8,9],[8,52],[6,24],[19,65],[7,48],[20,51],[2,21],[7,39],[11,27],[7,22],[12,6],[19,12],[12,66],[0,55],[20,62],[11,20],[2,35],[2,0],[6,7],[5,41],[9,37],[8,44],[16,15],[9,48],[18,54],[19,52],[19,24],[19,46],[5,0],[19,50],[2,37],[18,31],[6,20],[4,59],[5,39],[9,38],[19,51],[3,67],[11,33],[7,57],[13,47],[20,64],[8,24],[13,69],[4,11],[4,46],[13,32],[18,3],[20,54],[18,17],[7,5],[15,12],[12,7],[6,11],[5,4],[17,26],[7,12],[12,68],[8,45],[8,2],[15,34],[12,20],[1,26],[6,54],[19,16],[0,17],[9,13],[4,65],[12,58],[11,52],[8,32],[18,32],[11,50],[9,50],[17,13],[11,17],[16,53],[18,26],[2,42],[14,58],[0,23],[19,44],[9,39],[15,47],[11,70],[10,35],[8,41],[15,39],[20,50],[2,50],[17,39],[1,28],[7,63],[16,61],[15,58],[19,17],[11,40],[20,46],[12,41],[6,32],[2,67],[4,52],[14,24],[0,43],[17,34],[6,56],[2,53],[1,69],[0,11],[16,48],[1,47],[14,12],[7,23],[8,37],[17,18],[7,27],[7,2],[10,63],[13,6],[3,23],[12,8],[1,52],[11,30],[9,57],[16,57],[9,58],[4,38],[18,36],[10,17],[20,24],[13,64],[18,37],[4,21],[17,33],[2,33],[15,10],[8,40],[14,52],[19,1],[2,45],[11,55],[3,40],[8,31],[20,57],[6,33],[6,22],[6,28],[2,11],[4,15],[4,31],[16,26],[9,27],[10,61],[5,52],[3,68],[0,19],[13,40],[0,52],[18,22],[1,24],[13,29],[12,33],[16,58],[19,66],[6,62],[18,40],[17,58],[2,34],[15,63],[8,23],[14,50],[20,16],[6,9],[8,1],[3,0],[20,10],[15,23],[1,0],[13,4],[8,25],[10,13],[12,9],[18,39],[3,24],[20,63],[16,39],[7,36],[15,65],[13,10],[19,20],[3,54],[12,35],[17,49],[17,31],[14,48],[18,65],[2,44],[9,51],[17,64],[16,36],[7,10],[5,9],[12,13],[6,59],[13,21],[8,14],[10,67],[20,56],[6,53],[18,25],[14,39],[8,70],[10,27],[0,48],[0,36],[12,56],[3,28],[15,14]])
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