O(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q = deque()
                    q.append((i, j))
                    area = 0
                    while q:
                        x, y = q.popleft()
                        area += 1
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                                grid[nx][ny] = 0
                                q.append((nx, ny))
                    max_area = max(max_area, area)
        return max_area
