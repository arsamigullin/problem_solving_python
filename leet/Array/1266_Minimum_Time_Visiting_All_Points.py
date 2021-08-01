from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            ax = points[i - 1][0]
            ay = points[i - 1][1]
            bx = points[i][0]
            by = points[i][1]
            x = abs(bx - ax)
            y = abs(by - ay)
            res += max(x,y)

        return res
