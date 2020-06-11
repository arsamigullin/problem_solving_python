import collections
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def hasIsland(i, j):
            hasIsland = True
            q = collections.deque([(i, j)])
            while q:
                x, y = q.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    k, p = x + dx, y + dy
                    if 0 <= k < n and 0 <= p < m:
                        if grid[k][p] == 0 and (k, p) not in visited:
                            q.append((k, p))
                    else:
                        # IMPORTANT: once the p and k out of boundary
                        # do not return here from the function
                        # visit all the islands anyway
                        # If you will return here
                        # in the next visit it is possible to have visited islands
                        # but it will not go there because they are visited and at the same time they are located
                        # on boundary
                        # thereby it will return True (but since they are boundary islands the function must return
                        # False)
                        hasIsland = False
            return hasIsland

        count = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == 0:
                    if hasIsland(i, j):
                        # print(i,j)
                        count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    s.closedIsland([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]])