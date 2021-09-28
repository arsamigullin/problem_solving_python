from heapq import heappop, heappush, heapify


class Solution:
    def cherryPickup(self, grid) -> int:

        result = 0
        n = len(grid)
        m = len(grid[0])
        robot1 = [(-grid[0][0], 0, 0)]
        robot2 = [(-grid[0][m - 1], 0, m - 1)]
        visited = set()
        while True:
            val1, x1, y1 = heappop(robot1)
            val2, x2, y2 = heappop(robot2)
            if x1 == x2 and y1 == y2:
                result += abs(val1)
                while robot1 or robot2:
                    if robot1:
                        val1, x1, y1 = heappop(robot1)
                    if robot2:
                        val2, x2, y2 = heappop(robot2)
                    if abs(val2) > abs(val1):
                        result += abs(val2)
                        break
                    elif abs(val2) < abs(val1):
                        result += abs(val1)
                        break
                else:
                    result += abs(val2)
            else:
                result += abs(val1) + abs(val2)
            if x1 == n - 1 and x2 == n - 1:
                return result
            robot1 = []
            robot2 = []
            for i, j in [[x1 + 1, y1 - 1], [x1 + 1, y1 + 1], [x1 + 1, y1]]:
                if 0 <= i < n and 0 <= j < m:
                    heappush(robot1, (-grid[i][j], i, j))
            for i, j in [[x2 + 1, y2 - 1], [x2 + 1, y2 + 1], [x2 + 1, y2]]:
                if 0 <= i < n and 0 <= j < m:
                    heappush(robot2, (-grid[i][j], i, j))


if __name__ == '__main__':
    s = Solution()
    s.cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0],
                    [1, 0, 2, 3, 0, 0, 6]])
