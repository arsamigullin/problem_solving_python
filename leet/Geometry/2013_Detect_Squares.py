import collections
from typing import List


class DetectSquares:

    def __init__(self):
        self.all = collections.Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        self.all[(x,y)]+=1

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        tot = 0
        for (x3,y3), cnt in self.all.items():
            if abs(x1-x3)!=abs(y1-y3)  or (x1-x3) == 0:
                continue
            tot+= cnt * self.all[(x1,y3)]*self.all[(x3,y1)]
        return tot