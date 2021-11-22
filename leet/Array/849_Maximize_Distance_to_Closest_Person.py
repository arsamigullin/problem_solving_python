from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = 0
        n = len(seats)
        dist = 0
        for end in range(n):
            if seats[end] == 1:
                if start == 0:
                    dist = max(dist, end-start)
                else:
                    dist = max(dist, (end-start+1)//2)
                start = end + 1
        if seats[-1] == 0:
            dist = max(dist, end-start+1)
        return dist