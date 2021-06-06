import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        ef_sp = zip(efficiency, speed)
        # it is important step. We will have sorted by efficiency in Desc order array
        ef_sp = sorted(ef_sp, key=lambda x: x[0], reverse=True)
        print(ef_sp)
        speed_heap = []
        perf = 0
        sum_speed = 0
        for e, s in ef_sp:
            # since we first check and only then add to the queue, we use k-1 here
            # once we have a team of k members, before adding a new member
            if len(speed_heap) > k - 1:
                # we extract the member with the lowest speed
                sum_speed -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, s)
            sum_speed += s
            perf = max(perf, sum_speed * e)

        return perf % (10 ** 9 + 7)

if __name__ == '__main__':
    s = Solution()
    s.maxPerformance(6,[2,10,3,1,5,8],[5,4,3,9,7,2],2)