from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            count = 0

            # It will find consecutive ones horizontally
            for j in range(m):
                if mat[i][j]:
                    count += 1
                else:
                    count = 0
                dp[i][j] = count

        ans = 0

        for i in range(n):
            for j in range(m):

                # We will take min in that column
                mn = float('inf')
                for k in range(i, n):
                    mn = min(mn, dp[k][j])
                    ans += mn
        return ans


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        R, C = len(mat), len(mat[0])
        counts = [0] * C
        result = 0

        for row in mat:

            for j, v in enumerate(row):
                counts[j] = counts[j] + v if v else 0

            stack = []
            sums = [0] * C

            for j in range(C):

                while stack and counts[j] < counts[stack[-1]]:
                    stack.pop()

                if stack:
                    sums[j] = sums[stack[-1]]
                    sums[j] += counts[j] * (j - stack[-1])
                else:
                    sums[j] = counts[j] * (j + 1)

                result += sums[j]
                stack.append(j)

        return result

if __name__ == '__main__':
    s = Solution()
    s.numSubmat([[1,0,1],[1,1,0],[1,1,0]])