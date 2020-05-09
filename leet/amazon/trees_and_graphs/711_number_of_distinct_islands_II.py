import collections
from typing import List


class SolutionBFS:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        islands = set()
        n = len(grid)
        m = len(grid[0])

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = []
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        def bsf(i, j):
            island = set()
            init_i, init_j = i, j
            q = collections.deque([(i, j)])
            while q:
                x, y = q.popleft()
                if grid[x][y] == 0:
                    continue
                grid[x][y] = 0
                island.add(complex(x - init_i, y - init_j))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    k, p = x + dx, y + dy
                    if 0 <= k < n and 0 <= p < m and grid[k][p] == 1:
                        q.append((k, p))
            return tuple(island)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island = bsf(i, j)
                    if island:
                        islands.add(canonical(island))
        return len(island)


class Solution(object):
    def numDistinctIslands2(self, grid):
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = None
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)


class Solution3:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0]) if n else 0
        def dfs(i,j):
            if 0<=i<n and 0<=j<m and grid[i][j]==1:
                grid[i][j]=-1
                path.append([i,j])
                dfs(i,j+1)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i-1,j)

        def normalize(shape):
            possible_rotations=[[] for _ in range(8)]
            for x,y in shape:
                possible_rotations[0].append([x,y])
                possible_rotations[1].append([x,-y])
                possible_rotations[2].append([-x,y])
                possible_rotations[3].append([-x,-y])
                possible_rotations[4].append([y,x])
                possible_rotations[5].append([y,-x])
                possible_rotations[6].append([-y,x])
                possible_rotations[7].append([-y,-x])
            for r in possible_rotations:
                r.sort()
                x0,y0=r[0]
                for p in r:
                    p[0]-=x0
                    p[1]-=y0
            possible_rotations.sort()
            return tuple(c for r in possible_rotations[0] for c in r)
        res=set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    path=[]
                    dfs(i,j)
                    npath=normalize(path)
                    if len(npath)!=0:
                        # print("{}".format(npath))
                        res.add(npath)
        return len(res)


if __name__ == '__main__':
    s = Solution3()

    arr =  [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    ones = [(2,2),(2,3),(3,2)]
    # reset to zero to clearly see how the rotation will be displayed in array
    for i, j in ones:
        arr[i][j] = 0
    # collect all the possible rotations
    possible_rotations = [[] for _ in range(8)]
    for x, y in ones:
        possible_rotations[0].append([x, y])
        possible_rotations[1].append([x, -y])
        possible_rotations[2].append([-x, y])
        possible_rotations[3].append([-x, -y])
        possible_rotations[4].append([y, x])
        possible_rotations[5].append([y, -x])
        possible_rotations[6].append([-y, x])
        possible_rotations[7].append([-y, -x])

    for r in possible_rotations:
        r.sort()
        x0, y0 = r[0]
        for p in r:
            p[0] -= x0
            p[1] -= y0
    possible_rotations.sort()

    for possible_shape_rotation in possible_rotations:
        # put coordinates of possible rotation to the array
        for coordinate in possible_shape_rotation:
            i,j = coordinate
            arr[i][j] = 1
        print(arr)
        # clear the array for the next rotation
        for coordinate in possible_shape_rotation:
            i,j = coordinate
            arr[i][j] = 1


    #s.numDistinctIslands2([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]])