import bisect
import heapq
import math
from typing import List


class Solution1:
    def getSkyline(self, buildings):
        events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, None) for L, R, H in buildings)))
        # points is to store [x_left,H]
        # max_hight_heap is to store [-H,x_right]
        # events after sorting (one of the key points here is x1 and x2 are both mixed up here)
        # [(2, -10, 9), (3, -15, 7), (5, -12, 12), (7, 0, None), (9, 0, None), (12, 0, None), (15, -10, 20), (19, -8, 24), (20, 0, None), (24, 0, None)]
        '''
        1st iteration
        x, negH, R = 2,-10, 9
        getting rid of everything in heap, that is less than x and which has max Height
        heap = [[-10, 9]]
        points = [[2, 10]]
        
        2nd iteration
        heap = [[-15,7],[-10,9]]
        points = [[2,10],[3,15]]
        
        3rd iteration
        heap = [[-15,7],[-12, 12],[-10,9]]
        points = [[2,10],[3,15]]
        
        4th iteration
        x, negH, R = 7,0,None
        [-15,7] evicted from heap because 7>=7
        Since negH is 0, we do not add it to the max_height_heap
        heap = [[-12, 12],[-10,9]]
        however, -12 + 0 != 0, we add to the res [-12, 7]
        points = [[2,10],[3,15],[7,12]]
        
        5th iteration
        x, negH, R = 9,0,None
        because 9 <12 and no hight (0)
        heap is the same = [[-12, 12],[-10,9]]
        points are also the same because -12+12 = 0
        points = [[2,10],[3,15],[7,12]]
        
        6th iteration
        x, negH, R = 12,0,None
        heap = [] because x >= 12 amd 9
        no height, nothing to add to the heap
        0+0 = 0, nothing to add to the points
        res = [[2,10],[3,15],[7,12]]
        
        7th
        x, negH, R = 15,-10,20
        15 <= math.inf, nothing to evict
        There is a height here
        heap = [[-10, 20]]
        -10+12 > 0
        res = [[2,10],[3,15],[7,12],[15,10]]
        
        8th iteration      
        x, negH, R = 19,-8,24
        19<20, nothing to evict from heap
        there is a height here (-8), append (-8,24) to the heap
        heap = [[-10, 20],[-8,24]]
        since -10+10 = 0, nothing to add to the res
        res = [[2,10],[3,15],[7,12],[15,10]]
        
        9th iteration
        x, negH, R = 20, 0, None
        20 >=20 [-10, 20] evicted
        no height here
        heap = [[-8, 24]]
        since 10-8 > 0
        res = [[2,10],[3,15],[7,12],[15,10],[20,8]]
        
        10th iteration
        x, negH, R = 24, 0, None
        24>=24
        heap = [[0,max.inf]]
        0+max.inf > 0 current height (0) + math.inf > 0
        hence we add point [24,0], this zero was taken form heap[0][0]
        res = [[2,10],[3,15],[7,12],[15,10],[20,8],[24,0]]
        '''
        points, max_hight_heap = [[0, 0]], [(0, math.inf)]
        for x, negH, R in events:
            while x >= max_hight_heap[0][1]:
                heapq.heappop(max_hight_heap)
            if negH:
                heapq.heappush(max_hight_heap, (negH, R))
            if points[-1][1] + max_hight_heap[0][0]:
                points += [x, -max_hight_heap[0][0]],
        return points[1:]


from collections import defaultdict


class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        wtd = defaultdict(lambda: [[], []])
        for build in buildings:
            wtd[build[0]][0].append(build[2])
            wtd[build[1]][1].append(build[2])

        skyline = []
        cur_height = 0
        cur = []
        for loc in sorted(wtd):
            for rem in wtd[loc][1]:
                cur.pop(bisect.bisect_left(cur, rem))
            for add in wtd[loc][0]:
                bisect.insort(cur, add)
            new_height = cur[-1] if cur else 0
            if new_height != cur_height:
                cur_height = new_height
                skyline.append([loc, cur_height])
        return skyline


class Solution3:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        scan = [(l, -h, r) for l, r, h in buildings]
        scan += [(r, 0, 0) for _, r, _ in buildings]

        sky = [(0, 0)]
        alives = [(0, float('inf'))]
        from heapq import heappop, heappush
        for x, nh, r in sorted(scan):
            if nh < 0:
                heappush(alives, (nh, r))
            else:
                while alives[0][1] <= x:
                    heappop(alives)
            h = -alives[0][0]
            if h != sky[-1][1]:
                sky.append((x, h))
        return sky[1:]

if __name__ == '__main__':
    s = Solution1()
    s.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])