from typing import List

# greedy

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        stack = []
        for start, end in points:
            if not stack:
                stack.append([start, end])
            else:
                prev_start, prev_end = stack[-1]
                if prev_end >= start:
                    stack.pop()
                    stack.append([max(prev_start, start), min(prev_end, end)])
                else:
                    # stack.append([prev_start,prev_end])
                    stack.append([start, end])
        return len(stack)


from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        prev = points[0][1]
        res = 1
        for start, end in points:
            # if there is not intersection of interval
            # that means we need to have new arrow
            if prev<start:
                prev = end
                res += 1
        return res