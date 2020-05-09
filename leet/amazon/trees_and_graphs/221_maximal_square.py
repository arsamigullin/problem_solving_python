from typing import List

# brute force (mn)^2
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        def find(i, j):
            aim = 1
            while 0 <= i + aim < n and 0 <= j + aim < m:
                x1, y1 = i + aim, j
                x2, y2 = i, j + aim
                while y1 <= j + aim:
                    if matrix[x1][y1] == "1":
                        y1 += 1
                    else:
                        return aim
                while x2 <= i + aim:
                    if matrix[x2][y2] == "1":
                        x2 += 1
                    else:
                        return aim
                aim += 1
            return aim

        area = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    side = find(i, j)
                    area = max(area, side ** 2)
        return area

# O(mn)
# O(mn) space
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        Note, we start from matrix[1,1]
        and check if matrix[0][0] is 1.
        :param matrix:
        :return:

        Why do we need this check matrix[i - 1][j - 1] == "1"
        Consider this example
            0  1   2    3   4
       0 [["1","1","1","0","0"],
       1 ["1","0","1","1","1"],
       2 ["1","1","1","1","1"],
       3 ["1","0","0","1","0"]]

        dp[1][1] will contain 2, so it assumes that from starting from dp[1][1]
        towards top left there is a square with side 2

        now, let's assume we are at point 2,2. Since matrix[1][1] is not 1, it is no possible to have square
        without this check it would consider that the square is possible.

        NOTE: initially at dp[1][1] we always have 1, if matrix[0][0] == "1"

        dp[i][j] stores side length of the square which right bottom corner at matrix[i-1][j-1]

        '''
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        # note, in dp we have one row and one column more
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max_side = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    max_side = max(max_side, dp[i][j])
        print(dp)
        return max_side ** 2

# O(nm)
# O(m) space
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        max_square_len = 0
        dp = [0] * (ncols + 1)
        prev = 0

        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                tmp = dp[j]
                if (matrix[i - 1][j - 1] == '1'):
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    max_square_len = max(max_square_len, dp[j])
                else:
                    dp[j] = 0
                prev = tmp

        return max_square_len ** 2

if __name__ == '__main__':
    s = Solution()
    s.maximalSquare(
[["1","1"], ["1","0"]])
    s.maximalSquare(
        [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]]
    )

