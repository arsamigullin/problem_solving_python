# this is using monotonous stack technique
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
if __name__ == "__main__":
    s= Solution()
    s.trap([4,2,3])
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])

