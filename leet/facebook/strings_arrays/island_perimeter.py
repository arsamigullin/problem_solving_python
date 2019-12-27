# the solution quite strightforward
# if neighbor cell is out of boundary or this is water (0)
# increase total

class Solution:
    def islandPerimeter(self, grid) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    total += 1
                if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                    total += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    total += 1
                if j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                    total += 1
        return total
