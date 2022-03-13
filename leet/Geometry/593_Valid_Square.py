from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4: return False

        # Pythogorean theorem
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (y2 - y1) ** 2 + (x2 - x1) ** 2

        # we collect combinations
        D = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]
        # after sorting, sides will take the first 4 items, the last two are diagonal
        D.sort()
        return D[0] == D[1] == D[2] == D[3] and D[4] == D[5]
