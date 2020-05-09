from typing import List



class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        memo = {}
        n = len(A)
        m = len(A[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_score = float('inf')

        def dfs(i, j, pi, pj):
            nonlocal max_score
            if i == n - 1 and j == m - 1:
                max_score = min(A[i][j], max_score)
                return
            if (i, j) in memo:
                return
            memo[(i, j)] = True
            max_score = min(A[i][j], max_score)
            local_max = -1
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) != (pi, pj):
                    local_max = max(local_max, A[x][y])
            if local_max == -1:
                return
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and local_max == A[x][y] and (x, y) not in memo:
                    dfs(x, y, i, j)

        dfs(0, 0, -1, -1)
        return max_score


if __name__ == '__main__':
    s = Solution()
    s.maximumMinimumPath([[5,4,3,1],
                          [7,4,5,2],
                          [4,9,8,2],
                          [2,3,6,6]])