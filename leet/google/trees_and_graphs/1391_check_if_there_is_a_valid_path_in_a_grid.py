import collections

from leet.can_make_palindrome_from_substring import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        left = 0, -1
        right = 0, 1
        up = -1, 0
        down = 1, 0
        n = len(grid)
        m = len(grid[0])

        directions = {
            1: (right, left),
            2: (down, up),
            3: (left, down),
            4: (right, down),
            5: (left, up),
            6: (up, right),
        }
        expected = {
            (1, left): (1, 4, 6),
            (1, right): (1, 3, 5),
            (2, down): (2, 5, 6),
            (2, up): (2, 3, 4),
            (3, left): (1, 4, 6),
            (3, down): (2, 5, 6),
            (4, down): (2, 5, 6),
            (4, right): (1, 3, 5),
            (5, left): (1, 4, 6),
            (5, up): (2, 3, 4),
            (6, up): (2, 3, 4),
            (6, right): (1, 3, 5)
        }

        def bfs(i, j):
            q = collections.deque([(i, j)])
            while q:
                i, j = q.popleft()
                if grid[i][j] == -1:
                    continue
                if i == n - 1 and j == m - 1:
                    return True
                parent = grid[i][j]
                grid[i][j] = -1
                for direct in directions[parent]:
                    x, y = i + direct[0], j + direct[1]
                    if 0 <= x < n and 0 <= y < m:
                        child = grid[x][y]
                        if child in expected[(parent, direct)]:
                            q.append((x, y))
            return False

        def dfs(i, j):
            if grid[i][j] == -1:
                return False
            if i == n - 1 and j == m - 1:
                return True
            parent = grid[i][j]
            grid[i][j] = -1
            res = False
            for direct in directions[parent]:
                x, y = i + direct[0], j + direct[1]
                if 0 <= x < n and 0 <= y < m:
                    child = grid[x][y]
                    if child in expected[(parent, direct)]:
                        res |= dfs(x, y)
            return res

        return bfs(0, 0)



