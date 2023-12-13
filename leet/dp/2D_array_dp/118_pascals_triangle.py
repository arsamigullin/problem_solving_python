from typing import List


class Solution:
    def generate(self, numRows: int) -> list:
        result = []

        def get_pascal_triangle(n, prev):
            if n > numRows:
                return
            cur_res = [1] * n
            for i in range(len(prev) - 1):
                cur_res[i + 1] = prev[i] + prev[i + 1]
            result.append(cur_res)
            get_pascal_triangle(n + 1, cur_res)

        get_pascal_triangle(1, [])
        return result

    def generate_iterative(self, numRows: int) -> list:
        triangle = []

        for i in range(1, numRows + 1):
            current = [1] * i
            if len(triangle)>0:
                for j in range(len(triangle[-1]) - 1):
                    current[j + 1] = triangle[-1][j] + triangle[-1][j + 1]
            triangle.append(current)
        return triangle





if __name__ == "__main__":
    s = Solution()
    s.generate_iterative(5)