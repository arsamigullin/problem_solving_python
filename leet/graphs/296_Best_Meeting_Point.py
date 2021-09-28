import collections
import math
from typing import List


class SolutionTLE:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        visited = collections.defaultdict(set)
        queue = collections.deque()
        n = len(grid)
        m = len(grid[0])
        friend_count = 0
        friends = set()
        min_dist = math.inf
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    queue.append([friend_count, i, j, 0])
                    visited[(i, j)].add(friend_count)
                    grid[i][j] = 0
                    friend_count += 1
                    friends.add((i, j))

        while queue:
            friend_num, i, j, dist = queue.popleft()
            if len(visited[(i, j)]) == friend_count:
                min_dist = min(min_dist, grid[i][j])

            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < n and 0 <= y < m and friend_num not in visited[(x, y)]:
                    visited[(x, y)].add(friend_num)
                    grid[x][y] += dist + 1
                    queue.append((friend_num, x, y, dist + 1))

        return min_dist


class SolutionSorting:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        # rows.sort()
        # no need to sort rows, they are already sorted
        # the point under coordinate grid[row][col] is the best point
        row = rows[len(rows) // 2]
        cols.sort()
        col = cols[len(cols) // 2]
        # all we have to do  is to just calculate the distance between
        # every friend and best point
        def min_distance_1d(points, origin):
            distance = 0
            for point in points:
                distance += abs(point - origin)
            return distance

        return min_distance_1d(rows, row) + min_distance_1d(cols, col)

# the same as above but here we collect everything in sorting order
class SolutionCollectInSorting:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows.append(i)

        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    cols.append(j)

        # rows.sort()
        # no need to sort rows, they are already sorted
        row = rows[len(rows) // 2]
        col = cols[len(cols) // 2]

        def min_distance_1d(points, origin):
            distance = 0
            for point in points:
                distance += abs(point - origin)
            return distance

        return min_distance_1d(rows, row) + min_distance_1d(cols, col)


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        rows = []
        cols = []

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows.append(i)

        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    cols.append(j)

        def min_distance_1d(points):
            distance = 0
            i, j = 0, len(points) - 1
            while i < j:
                distance += points[j] - points[i]
                i += 1
                j -= 1
            return distance

        return min_distance_1d(rows) + min_distance_1d(cols)


if __name__ == '__main__':
    s = SolutionSorting()
    s.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])
    s.minTotalDistance([[0,1,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0],[1,1,1,0,1,0,1,0,0],[0,0,1,0,0,0,0,1,0],[1,0,1,1,0,1,0,0,0]])