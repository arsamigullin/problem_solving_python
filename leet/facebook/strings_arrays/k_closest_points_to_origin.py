import math
class Solution:
    def kClosest(self, points: list, K: int) -> list:
        arr = sorted(points, key=lambda item: math.sqrt(math.pow(item[0],2) + math.pow(item[1],2)))
        return arr[:K]