import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = [] # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # collect the climbs that equals ladders count
            # even if at the beginning of the array we have small climbs
            # and largest climbs are at the end of the array
            # since this is heap
            if len(ladder_allocations) <= ladders:
                continue
            # we will take out the smallest climb
            # and spend our bricks first
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1


class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # Helper function to check whether or not the specified building is reachable
        # from the first building with the bricks and ladders we have.
        def is_reachable(building_index):
            # Make a sorted list of all the climbs needed to get to the given building.
            climbs = []
            for h1, h2 in zip(heights[:building_index], heights[1:building_index + 1]):
                if h2 - h1 > 0:
                    climbs.append(h2 - h1)
            climbs.sort()
            # Check whether or not we have enough bricks and ladders to cover all
            # of these climbs. Bricks will be used before ladders.
            bricks_remaining = bricks
            ladders_remaining = ladders
            for climb in climbs:
                # If there are enough bricks left, use those.
                if climb <= bricks_remaining:
                    bricks_remaining -= climb
                # Otherwise, you'll have to use a ladder.
                elif ladders_remaining >= 1:
                    ladders_remaining -= 1
                # And if there are no ladders either, we can't reach buildingIndex.
                else:
                    return False
            return True

        # Do the binary search to find the final reachable building.
        lo = 0
        hi = len(heights) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if is_reachable(mid):
                lo = mid
            else:
                hi = mid - 1
        return hi  # Note that return lo would be equivalent.

if __name__ == '__main__':
    s = Solution()
    s.furthestBuilding([1,2,3,4,1,5,10000], 4, 1)
    s.furthestBuilding([4,2,7,6,9,14,12], 5, 1)
    s.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2)