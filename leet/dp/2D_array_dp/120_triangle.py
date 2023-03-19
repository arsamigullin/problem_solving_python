from typing import List
import  math

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def helper(i, j):
            if i >=n:
                return 0
            if (i,j) not in memo:
                memo[(i,j)] = math.inf
                for k in [j, j+1]:
                    if k<0 or k>=len(triangle[i]):
                        continue
                    memo[(i,j)] = min(memo[(i,j)], helper(i+1, k)  + triangle[i][k])
            return memo[(i,j)]

        return helper(0,0)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = [0]

        for i in range(n):
            cur = [0] * (len(triangle[i])+1)
            for j in range(len(triangle[i])):
                if j + 1 < len(prev) and j > 0 :
                    cur[j+1] = min(prev[j+1], prev[j]) + triangle[i][j]
                elif j + 1 < len(prev):
                    cur[j+1] = prev[j+1] + triangle[i][j]
                else:
                    cur[j+1] = prev[j] + triangle[i][j]
            prev = cur
        return min(prev[1:])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev_row = triangle[-1]

        # prev_row is always 1 item longer the cur one
        for i in reversed(range(n-1)):
            cur = []
            for j in range(len(triangle[i])):
                min_of_two = min(prev_row[j], prev_row[j+1])
                cur.append(min_of_two + triangle[i][j])
            prev_row = cur
        return prev_row[0]
