import heapq
from typing import List


class MySolution:
    def minAvailableDuration(self, slot1: List[List[int]], slot2: List[List[int]], duration: int) -> List[int]:
        n1 = len(slot1)
        n2 = len(slot2)
        i = j = 0
        slot1.sort()
        slot2.sort()
        while i<n1 and j<n2:
            s1,e1=slot1[i]
            s2,e2=slot2[j]
            s = max(s1,s2)
            e = min(e1, e2)
            if e - s >= duration:
                return [s, s + duration]
            if e1>e2:
                j+=1
            else:
                i+=1
        return []


class SolutionHeap:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # build up a heap containing time slots last longer than duration
        timeslots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(timeslots)

        while len(timeslots) > 1:
            start1, end1 = heapq.heappop(timeslots)
            start2, end2 = timeslots[0]
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        return []

if __name__ == '__main__':
    s = SolutionHeap()
    s.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)