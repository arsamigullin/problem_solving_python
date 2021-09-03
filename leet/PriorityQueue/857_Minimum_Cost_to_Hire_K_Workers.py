import math
from typing import List
from fractions import Fraction
import heapq

'''
Important to understand here these conditions
1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
2. Every worker in the paid group must be paid at least their minimum-wage expectation.
The key words in the first condition is "paid" and "ratio of their quality"
Every worker has its wage/quality ratio. So, it at least should be paid its wage and according to the worker's ratio

To achieve this we need to undersand this
wi/qi = wtot/qtot
The ratio between total wage and total quality should be at least the same (also could be greater) than ratio
between ith worker wage and ith worker quality

from that follows
wtot = (wi/qi) * qtot

let's denote wi/qi as r. it can be precalculated in advance
wtot = r * qtot

then important to sort the precalculated ratios because based on this formula
we want to collect the people with the least ration

At each iteration we we contribute the ith worker quality to the total quality and r is precalculated already
wtot is calculated ones we reached K

Once the num workers is greater than K, we subtract the highest quality of the worker that previously contributed
to the total quality (maintained by max heap)

NOTE: since we sorted the ratios, the workers 0 ... i-1 will be paid even more (because their ratio is less than the ith worker)
and only ith worker will receive at least its min wage

'''


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

        ratio_quality = sorted([(w / q, q) for w, q in zip(wage, quality)])

        heap = []
        tot_quality = 0
        tot_wage = math.inf
        for r, q in ratio_quality:
            tot_quality += q
            heapq.heappush(heap, -q)
            if len(heap) > k:
                tot_quality += heapq.heappop(heap)
            if len(heap) == k:
                tot_wage = min(tot_wage, r * tot_quality)
        return tot_wage

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)



if __name__ == '__main__':
    s =Solution()
    s.mincostToHireWorkers([10, 5], [70, 30], 2)
    s.mincostToHireWorkers([10,20,5], [70,50,30], 2)