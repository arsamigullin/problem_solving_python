# precalc
from typing import List


class PascalTriangle:

    def __init__(self):
        self.triangle = [[1]]
        for i in range(33):
            prev = self.triangle[-1]
            cur = [0] * (len(prev) + 1)
            for j in range(len(cur)):
                first = prev[j - 1] if j - 1 >= 0 else 0
                second = prev[j] if j < len(prev) else 0
                cur[j] = first + second
            self.triangle.append(cur)


class Solution:
    t = PascalTriangle()

    def getRow(self, rowIndex: int) -> List[int]:
        return self.t.triangle[rowIndex]


# yet another iterative
class Solution:
    t = PascalTriangle()

    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(rowIndex):
            cur = [0] * (len(prev) + 1)
            for j in range(len(cur)):
                first = prev[j - 1] if j - 1 >= 0 else 0
                second = prev[j] if j < len(prev) else 0
                cur[j] = first + second
            prev = cur
        return prev
