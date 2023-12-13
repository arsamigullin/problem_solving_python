# 1st closely read the description
# A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).
from typing import List


# isosceles triangle property
# https://mathvox.com/geometry/triangles/chapter-5-right-triangle/the-right-isosceles-triangle/
class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        stack = []
        max_right_point = 0
        for x, y in sorted(peaks):
            # based on isosceles triangle properties we can find two other points of the triangle
            left_point = x - y
            right_point = x + y

            # if there is a left point which is more left, extract all other points because the triangles won't be visible

            while stack and stack[-1] >= left_point:
                stack.pop()

            if right_point > max_right_point:
                max_right_point = right_point
                stack.append(left_point)

        return len(stack)
