# this problem
# https://leetcode.com/problems/rectangle-area/

# related problem
# https://leetcode.com/problems/rectangle-overlap/

class Solution:
    '''
    if we have an overlap than it will be formed the way defined below
    '''
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        # find the square of rectangles
        first = (C - A) * (D - B)
        second = (G - E) * (H - F)

        overlap_w1 = max(A, E)
        overlap_w2 = min(C, G)
        overlap_h1 = max(B, F)
        overlap_h2 = min(D, H)
        w = overlap_w2 - overlap_w1
        h = overlap_h2 - overlap_h1
        if w < 0 or h < 0:
            overlap = 0
        else:
            overlap = w * h

        return first + second - overlap