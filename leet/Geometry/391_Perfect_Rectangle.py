from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        area_func = lambda a, b: a * b
        area = 0
        # this is collection of corners
        corners = set()
        for a, b, x, y in rectangles:
            area += area_func(x - a, y - b)
            # this is XOR, as we know XOR on the same numbers is 0
            # this allows us to eliminate the adjacent corners, so only 4 corners left
            corners ^= {(a, y), (a, b), (x, b), (x, y)}

        # otherwise it is false
        if len(corners) != 4:
            return False

        # rectangle formed by the left four corner should have the same area as all rectangles
        # inside of the left corners

        a, b = min(corners, key=lambda x: x[0] + x[1])
        x, y = max(corners, key=lambda x: x[0] + x[1])

        return area_func(x - a, y - b) == area
