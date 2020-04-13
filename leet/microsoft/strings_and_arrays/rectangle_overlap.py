# this problem
# https://leetcode.com/problems/rectangle-overlap/

import typing
List = typing.List

class Solution:
    '''
    if we have an overlap than it will be formed the way defined below
    '''
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        overlap_w1 = max(x1, a1)
        overlap_w2 = min(x2, a2)
        overlap_h1 = max(y1, b1)
        overlap_h2 = min(y2, b2)

        # the overlap exists only if both w and h are greater 0
        w = overlap_w2 - overlap_w1
        h = overlap_h2 - overlap_h1
        return w > 0 and h > 0