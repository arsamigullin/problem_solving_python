import collections
from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])
        dp = [[[0] * 4 for j in range(m)] for _ in range(n)]
        max_line = 0
        for i in range(n):
            for j in range(m):
                cur = dp[i][j]
                if mat[i][j] == 1:
                    cur[0] = dp[i][j - 1][0] + 1 if j - 1 >= 0 else 1
                    cur[1] = dp[i - 1][j][1] + 1 if i - 1 >= 0 else 1
                    cur[2] = dp[i - 1][j - 1][2] + 1 if i - 1 >= 0 and j - 1 >= 0 else 1
                    cur[3] = dp[i - 1][j + 1][3] + 1 if i - 1 >= 0 and j + 1 < m else 1
                max_line = max(max_line, max(cur))
        return max_line


class Solution1:
    def longestLine(self, mat: List[List[int]]) -> int:

        rowd = collections.defaultdict(int)
        cold = collections.defaultdict(int)
        diag = collections.defaultdict(int)
        adiag = collections.defaultdict(int)

        n = len(mat)
        m = len(mat[0])
        max_line = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rowd[i] += 1
                    cold[j] += 1
                    diag[i + j] += 1
                    adiag[i - j] += 1
                    max_line = max(max_line, rowd[i], cold[j], diag[i + j], adiag[i - j])
                else:
                    rowd[i] = cold[j] = diag[i + j] = adiag[i - j] = 0

        return max_line

if __name__ == '__main__':
    s = Solution1()
    s.longestLine([[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]])
    s.longestLine([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
