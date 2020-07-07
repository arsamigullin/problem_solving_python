from typing import List


class NumMatrix:

    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0])== 0:
            return
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # this is the formula for prefix sum of 2D array
                # left element + top element + prev item from orig matrix - diagonal element
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

        print('done')


    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1];


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.arr = None
            return
        n = len(matrix)
        m = len(matrix[0])
        self.arr = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.arr[i + 1][j + 1] = self.arr[i + 1][j] + matrix[i][j]

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                self.arr[i][j] += self.arr[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.arr:
            return 0
        return self.arr[row2 + 1][col2 + 1] - self.arr[row2 + 1][col1] - (
                    self.arr[row1][col2 + 1] - self.arr[row1][col1])

# damn solution
class NumMatrixMyWeirdSolution:

    def __init__(self, matrix):
        self.matrix = matrix
        if len(matrix) == 0:
            return
        if len(matrix) == 1:
            self.sm = [[0] * len(matrix[0]) for _ in range(1)]
            self.sm[0][0] = matrix[0][0]
            for i in range(1, len(matrix[0])):
                self.sm[0][i] = self.sm[0][i - 1] + matrix[0][i]
            return
        self.sm = [[0] * len(matrix) for _ in range(len(matrix))]
        self.sm[0][0] = matrix[0][0]
        for i in range(1, len(matrix[0])):
            self.sm[0][i] = matrix[0][i]
        for i in range(1, len(matrix)):
            self.sm[i][0] = matrix[i][0]
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.sm[i][j] = matrix[i][j] + self.sm[i][j - 1]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                self.sm[i][j] += self.sm[i - 1][j]
        print('done')

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if len(self.matrix) == 0:
            return 0
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        if row1 - 1 < 0 and col1 - 1 < 0:
            return self.matrix[row2][col2]
        if row1 == row2:
            if col1-1 < 0:
                return self.sm[row2][col2]
            else:
                return self.sm[row2][col2] - self.sm[row1][col1 - 1]
        if col1 == col2:
            if row1 - 1 < 0:
                return self.sm[row2][col2]
            else:
                return self.sm[row2][col2] - self.sm[row1 - 1][col1]

        if row1 - 1 < 0:
            return self.sm[row2][col2] - self.sm[row2][col1-1]
        elif col1 - 1 < 0:
            return self.sm[row2][col2] - self.sm[row1 - 1][col2]
        else:
            return self.sm[row2][col2] - (self.sm[row2][col1-1] -
                                          self.sm[row1 - 1][col1 - 1]) - self.sm[row1 - 1][col2]

if __name__ == "__main__":

    #s = NumMatrix([[8,-4,5],[-1,4,4],[-2,3,1],[-4,4,3]])
    #s.sumRegion(0,1,0,2)
    s = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    s.sumRegion(2, 1, 4, 3)