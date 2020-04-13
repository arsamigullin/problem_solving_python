#https://leetcode.com/problems/maximize-distance-to-closest-person/
# we gather busy seats and calculate distance between them

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        busy = [i for i in range(len(seats)) if seats[i] == 1]
        max_dist = float('-inf')
        # do not forget to check boundaries
        if seats[0] == 0:
            max_dist = max(max_dist, busy[0])
        # do not forget to check boundaries
        if seats[-1] == 0:
            max_dist = max(max_dist, len(seats) - busy[-1] - 1)

        for i in range(len(busy) - 1):
            max_dist = max(max_dist, (busy[i + 1] - busy[i]) // 2)
        return max_dist