from typing import List


class Solution1:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        cnt = 0

        def helper(i, j, num):
            nonlocal cnt
            res = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] == -1 or grid[x][y] == 3:
                        continue
                    if grid[x][y] == 2:
                        res |= 1 << 0
                        continue
                    res |= 1 << 1
                    grid[x][y] = 3
                    found = helper(x, y, num - 1)
                    grid[x][y] = 0
                    if found and not (i==0 and j==0):
                        return True
            if res == 1 and num == 0:
                cnt += 1
                return True
            return False

        empty = 0
        start = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = i, j
                if grid[i][j] == 0:
                    empty += 1
        helper(start[0], start[1], empty)
        return cnt

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        cnt = 0

        def helper(i, j, num):
            nonlocal cnt
            if grid[i][j] == 2:
                if num == 0:
                    cnt+=1
                return
            grid[i][j] = 3
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] == -1 or grid[x][y] == 3:
                        continue
                    helper(x, y, num - 1)
            grid[i][j] = 0

        empty = 0
        start = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = i, j
                if grid[i][j] == 0:
                    empty += 1
        helper(start[0], start[1], empty)
        return cnt

if __name__ == '__main__':
    s = Solution()
    s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])

