import collections
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # d = collections.defaultdict(int)
        dr = collections.defaultdict(int)
        n = len(mat)
        m = len(mat[0])
        mid_n = n // 2
        mid_m = m // 2
        answer = [[0] * m for _ in range(n)]
        c = [[0] * (m + 1) for _ in range(n + 1)]
        b = [[0] * (m + 1) for _ in range(n + 1)]
        d = [[0] * (m + 1) for _ in range(n + 1)]
        e = [[0] * (m + 1) for _ in range(n + 1)]
        # for i in range(n):
        #     for j in range(m):
        #         #c[i][j] = mat[i][j]
        #         b[i][j] = mat[i][j]
        #         d[i][j] = mat[i][j]
        #         e[i][j] = mat[i][j]
        # from left to bottom
        for i in range(n):
            for j in range(m):
                c[i + 1][j + 1] += c[i + 1][j] + mat[i][j]

        for j in range(m):
            for i in range(1, n):
                c[i][j] += c[i - 1][j]

        # from right to bottom
        for i in range(n):
            for j in range(m - 1, -1, -1):
                b[i + 1][j] += b[i + 1][j + 1] + mat[i][j]

        for j in range(m):
            for i in range(1, n):
                b[i][j] += b[i - 1][j]

                # from bottom to left
        for j in range(m):
            for i in range(n - 1, -1, -1):
                d[i][j] += d[i + 1][j] + mat[i][j]
                # print(d)
        for i in range(n):
            for j in range(m - 1, -1, -1):
                d[i][j] += d[i][j + 1]

                # from bottom to right
        for j in range(m):
            for i in range(n - 1, -1, -1):
                e[i][j + 1] += e[i + 1][j + 1] + mat[i][j]
        # print(e)
        for i in range(n):
            for j in range(m):
                e[i][j + 1] += e[i][j]

        print(c)
        print(b)
        print(d)
        print(e)

        for i in range(n):
            for j in range(m):
                x, y = min(i + K, n - 1), min(j + K, m - 1)
                p, q = max(i - K, 0), max(j - K, 0)
                if i <= mid_n and j <= mid_m:
                    answer[i][j] = c[x+1][y+1] - c[p][y+1]
                elif i > mid_n and j > mid_m:
                    answer[i][j] = d[p][q]
                elif j > mid_m:
                    answer[i][j] = b[x][q]
                elif i > mid_n:
                    answer[i][j] = e[p][y]

        return answer


class Solution1:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # d = collections.defaultdict(int)
        dr = collections.defaultdict(int)
        n = len(mat)
        m = len(mat[0])
        mid_n = n // 2
        mid_m = m // 2
        answer = [[0] * m for _ in range(n)]
        c = [[0] * m for _ in range(n)]
        b = [[0] * m for _ in range(n)]
        d = [[0] * m for _ in range(n)]
        e = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                c[i][j] = mat[i][j]
                b[i][j] = mat[i][j]
                d[i][j] = mat[i][j]
                e[i][j] = mat[i][j]
        # from left to bottom
        for i in range(n):
            for j in range(1, m):
                c[i][j] += c[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                c[i][j] += c[i - 1][j]

                # from right to bottom
        for i in range(n):
            for j in range(m - 2, -1, -1):
                b[i][j] += b[i][j + 1]

        for j in range(m):
            for i in range(1, n):
                b[i][j] += b[i - 1][j]

                # from bottom to left
        for j in range(m):
            for i in range(n - 2, -1, -1):
                d[i][j] += d[i + 1][j]

        for i in range(n):
            for j in range(m - 2, -1, -1):
                d[i][j] += d[i][j + 1]

                # from bottom to right
        for j in range(m):
            for i in range(n - 2, -1, -1):
                e[i][j] += e[i + 1][j]
        for i in range(n):
            for j in range(1, m):
                e[i][j] += e[i][j - 1]

        print(c)
        print(b)
        print(d)
        print(e)

        for i in range(n):
            for j in range(m):
                x, y = min(i + K, n - 1), min(j + K, m - 1)
                p, q = max(i - K, 0), max(j - K, 0)
                if i <= mid_n and j <= mid_m:
                    answer[i][j] = c[x][y]
                elif i > mid_n and j > mid_m:
                    answer[i][j] = d[p][q]
                elif j > mid_m:
                    answer[i][j] = b[x][q]
                elif i > mid_n:
                    answer[i][j] = e[p][y]

        return answer


class Solution2:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # d = collections.defaultdict(int)
        dr = collections.defaultdict(int)
        n = len(mat)
        m = len(mat[0])
        mid_n = n // 2
        mid_m = m // 2
        answer = [[0] * m for _ in range(n)]
        c = [[0] * m for _ in range(n)]
        b = [[0] * m for _ in range(n)]
        d = [[0] * m for _ in range(n)]
        e = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                c[i][j] = mat[i][j]
                b[i][j] = mat[i][j]
                d[i][j] = mat[i][j]
                e[i][j] = mat[i][j]
        # from left to bottom
        for i in range(n):
            for j in range(1, m):
                c[i][j] += c[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                c[i][j] += c[i - 1][j]

                # from right to bottom
        for i in range(n):
            for j in range(m - 2, -1, -1):
                b[i][j] += b[i][j + 1]

        for j in range(m):
            for i in range(1, n):
                b[i][j] += b[i - 1][j]

                # from bottom to left
        for j in range(m):
            for i in range(n - 2, -1, -1):
                d[i][j] += d[i + 1][j]

        for i in range(n):
            for j in range(m - 2, -1, -1):
                d[i][j] += d[i][j + 1]

                # from bottom to right
        for j in range(m):
            for i in range(n - 2, -1, -1):
                e[i][j] += e[i + 1][j]
        for i in range(n):
            for j in range(1, m):
                e[i][j] += e[i][j - 1]

        for i in range(n):
            for j in range(m):
                x, y = min(i + K, n - 1), min(j + K, m - 1)
                p, q = max(i - K, 0), max(j - K, 0)
                if i <= mid_n and j <= mid_m:
                    answer[i][j] = c[x][y]
                elif i > mid_n and j > mid_m:
                    answer[i][j] = d[p][q]
                elif j > mid_m and i <= mid_n:
                    answer[i][j] = b[x][q]
                elif i > mid_n and j <= mid_m:
                    answer[i][j] = e[p][y]

        # print(c)
        # print(b)
        # print(d)
        # print(e)

        return answer


class Solution3:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        # d = collections.defaultdict(int)
        dr = collections.defaultdict(int)
        n = len(mat)
        m = len(mat[0])
        mid_n = n // 2
        mid_m = m // 2
        answer = [[0] * m for _ in range(n)]
        c = [[0] * m for _ in range(n)]
        b = [[0] * m for _ in range(n)]
        d = [[0] * m for _ in range(n)]
        e = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                c[i][j] = mat[i][j]
                b[i][j] = mat[i][j]
                d[i][j] = mat[i][j]
                e[i][j] = mat[i][j]
        # from left to bottom
        for i in range(n):
            for j in range(1, m):
                c[i][j] += c[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                c[i][j] += c[i - 1][j]

                # from right to bottom
        for i in range(n):
            for j in range(m - 2, -1, -1):
                b[i][j] += b[i][j + 1]

        for j in range(m):
            for i in range(1, n):
                b[i][j] += b[i - 1][j]

                # from bottom to left
        for j in range(m):
            for i in range(n - 2, -1, -1):
                d[i][j] += d[i + 1][j]

        for i in range(n):
            for j in range(m - 2, -1, -1):
                d[i][j] += d[i][j + 1]

                # from bottom to right
        for j in range(m):
            for i in range(n - 2, -1, -1):
                e[i][j] += e[i + 1][j]
        for i in range(n):
            for j in range(1, m):
                e[i][j] += e[i][j - 1]

        for i in range(n):
            for j in range(m):
                x, y = min(i + K, n - 1), min(j + K, m - 1)
                p, q = max(i - K, 0), max(j - K, 0)
                if i <= mid_n and j <= mid_m:
                    answer[i][j] = c[x][y] - (0 if i - K - 1 < 0 else c[i - K - 1][y])
                elif i > mid_n and j > mid_m:
                    answer[i][j] = d[p][q] - (0 if i + K + 1 >=n else d[i + K + 1][q])
                elif j > mid_m and i <= mid_n:
                    answer[i][j] = b[x][q] - (0 if i - K - 1 < 0 else b[i - K - 1][q])
                elif i > mid_n and j <= mid_m:
                    answer[i][j] = e[p][y] - (0 if i + K + 1 >=n else e[i + K + 1][y])

        # print(c)
        # print(b)
        # print(d)
        # print(e)

        return answer


if __name__ == '__main__':
    s = Solution3()
    s.matrixBlockSum([[76,4,73],[21,8,56],[4,56,61],[70,32,38],[31,94,67]], 1)