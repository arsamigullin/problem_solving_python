# https://leetcode.com/problems/container-with-most-water/
# We always will be limited with min height of container
class Solution:
    def maxArea(self, height: list) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if height[i] >= height[j]:
                j-=1
            else:
                i+=1
        return area