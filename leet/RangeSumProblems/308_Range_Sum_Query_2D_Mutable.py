from typing import List

# this is not effective solution
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.arr = matrix
        self.dp = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        # print(self.n, self.m)
        self.refresh(0, 0)

    def update(self, row: int, col: int, val: int) -> None:
        self.arr[row][col] = val
        self.refresh(row, col)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - (self.dp[row1][col2 + 1] - self.dp[row1][col1])

    def refresh(self, x, y):
        for i in range(x, self.n):
            for j in range(y, self.m):
                self.dp[i + 1][j + 1] = self.dp[i][j + 1] + self.dp[i + 1][j] + self.arr[i][j] - self.dp[i][j]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)