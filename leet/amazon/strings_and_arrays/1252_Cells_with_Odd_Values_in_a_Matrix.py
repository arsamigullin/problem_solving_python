from typing import List


class Solution1:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        arr = [[0] * m for _ in range(n)]
        odds = 0
        for i, j in indices:
            for k in range(m):
                arr[i][k] += 1
                odds += -1 if arr[i][k] % 2 == 0 else 1
            for k in range(n):
                arr[k][j] += 1
                odds += -1 if arr[k][j] % 2 == 0 else 1
        return odds


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        res = 0
        xs = {i: 0 for i in range(n)}
        ys = {i: 0 for i in range(m)}
        for ri, ci in indices:
            xs[ri] += 1
            ys[ci] += 1
        for r in range(n):
            x_val = xs[r]
            for c in range(m):
                if (x_val + ys[c]) % 2 == 1:
                    res += 1
        return res