# this is using monotonous stack technique
from typing import List


class Solution:
    def trap(self, height: list) -> int:
        s = [-1]
        res = 0
        for i in range(len(height)):
            # stack holds decreasing sequence
            while s[-1] != -1 and height[s[-1]] < height[i]:
                # j represents the bottom of capacity
                # s[-1] is the left wall
                # height[i] is the right wall
                # we must take minimum height of walls
                j = s.pop()
                if s[-1] == -1:
                    break
                area = (min(height[s[-1]], height[i]) - height[j]) * (i - s[-1] - 1)
                if area > 0:
                    res += area
            s.append(i)
        return res


class Solution1:
    def trap(self, height: List[int]) -> int:

        stack = [-1]
        area = 0
        for i, h in enumerate(height):
            while stack[-1] != -1 and stack[-1][0] < h:
                prevH, j = stack.pop()
                if stack[-1] == -1:
                    break
                lastH, k = stack[-1]
                width = i - k - 1
                height = min(lastH, h) - prevH
                area += height * width

            stack.append((h, i))
        return area

if __name__ == "__main__":
    s= Solution1()
    s.trap([1,0,0,0,1])
    s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    s.trap([4,2,3])


