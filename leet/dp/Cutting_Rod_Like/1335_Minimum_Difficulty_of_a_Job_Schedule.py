from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        if d > n:
            return -1
        M = 10 ** 10 + 1
        memo = {}

        def dfs(i, d):
            if i >= n and d == 0:
                return 0
            if d == 0:
                return M
            if (i, d) not in memo:
                m = -1
                res = M
                for j in range(i, n):
                    m = max(jobDifficulty[j], m)
                    res = min(res, dfs(j + 1, d - 1) + m)
                memo[(i, d)] = res
            return memo[(i, d)]

        return dfs(0, d) 