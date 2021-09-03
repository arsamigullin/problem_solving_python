from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])
        memo = [[0] * m for _ in range(n)]
        def dfs(i, j):
            if memo[i][j] == 0:
                cur_val = matrix[i][j]
                count = 1
                # the reason we do not detect cycle is this condition matrix[i][j] < matrix[x][y]
                # if we came to 8 from 4, we never will go back to 4 since 8>4
                # this helps us to avoid visited structure
                for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= x < n and 0 <= y < m and matrix[x][y] > cur_val:
                        count = max(count, dfs(x, y) + 1)
                memo[i][j] = count
            return memo[i][j]

        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))

        return res


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        mem = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        n = len(matrix)
        m = len(matrix[0])

        def dfs(i, j):
            if mem[i][j] != 0:
                return mem[i][j]
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + di
                y = j + dj
                # the reason we do not detect cycle is this condition matrix[i][j] < matrix[x][y]
                # if we came to 8 from 4, we never will go back to 4 since 8>4
                # this helps us to avoid visited structure
                if 0 <= x < n and 0 <= y < m and matrix[i][j] < matrix[x][y]:
                    mem[i][j] = max(mem[i][j], dfs(x, y))
            mem[i][j] += 1
            return mem[i][j]

        _max = 0
        for i in range(n):
            for j in range(m):
                _max = max(_max, dfs(i, j))
        return _max

# topological sort
# there is not fully understanding of that approach
#  will comment only what is understood
class SolutionOnionPeeling:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        matrix = [[0] * (n + 2) for _ in range(m + 2)]

        # matrix will be as grid but with zeros around, i.e.
        # [0, 0, 0, 0, 0]
        # [[0, 9, 9, 4, 0],
        # [0, 6, 6, 8, 0],
        # [0, 2, 1, 1, 0]
        # [0, 0, 0, 0, 0]
        for i in range(m):
            matrix[i + 1][1:n + 1] = grid[i]

        # has the same size as matrix but contains
        # but instead of values contains the numbers that
        # indecate how many neighbors this current number is less than neighbors
        # for the matrix above the outdegree array will be as following:
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 2, 0]
        # [0, 1, 2, 0, 0]
        # [0, 1, 2, 1, 0]
        # [0, 0, 0, 0, 0]
        # number 2 in outdegree[1][3] means there are two neighbors that
        # have values greater than [1][3]
        # indeed, for number 4 there are two neighbors 8 and 9
        outdegree = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for di, dj in dirs:
                    if matrix[i][j] < matrix[i + di][j + dj]:
                        outdegree[i][j] += 1

        leaves = []
        m += 2
        n += 2
        # starting from outdegree[1][1]
        # we collect all the points with value 0
        # in our case they are 3 in total
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if outdegree[i][j] == 0:
                    leaves.append((i, j))

        height = 0
        while leaves:
            height += 1
            newleaves = []
            for x, y in leaves:
                for dx, dy in dirs:
                    i = x + dx
                    j = y + dy
                    if matrix[x][y] > matrix[i][j]:
                        outdegree[i][j] -= 1
                        if outdegree[i][j] == 0:
                            newleaves.append((i, j))
            leaves = newleaves

        # here is the transformation of outdegree

        # after first iteration
        # [[0, -1, -1, 0, 0],
        # [-1, 0, 0, 0, 0],
        # [0, 0, 0, 0, -1],
        # [0, 1, 2, 0, 0],
        # [0, 0, 0, 0, 0]]

        # after second iteration
        # [[0, -1, -1, -1, 0],
        # [-1, 0, 0, 0, -1],
        # [-1, 0, 0, 0, -1],
        # [0, 0, 1, 0, -1],
        # [0, 0, 0, -1, 0]]

        # after third
        # [[0, -1, -1, -1, 0],
        # [-1, 0, 0, 0, -1],
        # [-1, 0, 0, 0, -1],
        # [-1, 0, 0, 0, -1],
        # [0, -1, 0, -1, 0]]

        # after fourth
        # [[0, -1, -1, -1, 0],
        # [-1, 0, 0, 0, -1],
        # [-1, 0, 0, 0, -1],
        # [-1, 0, 0, 0, -1],
        # [0, -1, -1, -1, 0]]

        return height

if __name__ == '__main__':
    s = SolutionOnionPeeling()
    s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
