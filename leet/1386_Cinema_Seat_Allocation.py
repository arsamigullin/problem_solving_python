import collections
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        aisleSeatsDict = collections.defaultdict(set)
        for row, seat in reservedSeats:
            aisleSeatsDict[row - 1].add(seat - 1)
        left_spot = {1, 2, 3, 4}
        right_spot = {5, 6, 7, 8}
        middle_spot = {3, 4, 5, 6}
        tot = 0
        for aisle in aisleSeatsDict:
            groups = 0
            if left_spot.difference(aisleSeatsDict[aisle]) == left_spot:
                groups += 1
            if right_spot.difference(aisleSeatsDict[aisle]) == right_spot:
                groups += 1
            if groups == 0 and middle_spot.difference(aisleSeatsDict[aisle]) == middle_spot:
                groups += 1
            tot += groups

        return tot + (n - len(aisleSeatsDict)) * 2


