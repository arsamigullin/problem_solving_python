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

# O(3^N)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        start = 0
        target = 0
        non_obstacles = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    non_obstacles += 1
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    target = (i, j)

        count = 0

        def backtrack(i, j, remains):
            nonlocal count
            if i == target[0] and j == target[1] and remains == 0:
                count += 1
                return
            tmp = grid[i][j]
            grid[i][j] = -3
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = dx + i
                y = dy + j
                if 0 <= x < n and 0 <= y < m and grid[x][y] >= 0:
                    backtrack(x, y, remains - 1)
            grid[i][j] = tmp

        backtrack(start[0], start[1], non_obstacles + 1)
        return count


if __name__ == '__main__':
    s = Solution()
    s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])

