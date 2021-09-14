import collections
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:linear-equations-graphs/x2f8bb11595b61c86:slope/a/slope-review
        # the solution is based on the slope
        # if slope of three points is the same, then they are on the same line
        res = 0
        while points:
            x1, y1 = points.pop()
            slopes = collections.defaultdict(int)
            dups = 1
            cur_max = 0
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    dups += 1
                else:
                    slope = (y1 - y2) / (x1 - x2) if x1 != x2 else math.inf
                    slopes[slope] += 1
                    cur_max = max(cur_max, slopes[slope])
            res = max(res, cur_max + dups)
        return res