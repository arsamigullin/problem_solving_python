import heapq
from typing import List


class SolutionMy:
    def minCost(self, s: str, cost: List[int]) -> int:

        heap = []
        res = 0
        for i in range(len(s)):
            heapq.heappush(heap, cost[i])
            if i == len(s) - 1 or s[i] != s[i + 1]:
                while len(heap) > 1:
                    res += heapq.heappop(heap)
                heap = []
        return res


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        l = 0
        r = 1
        n = len(s)
        curr = s[0]
        res = 0

        def calculate(l, r):
            return sum(cost[l:r]) - max(cost[l:r])

        while r < n:
            if s[r] == curr:
                r += 1
            else:
                res += calculate(l, r)

                curr = s[r]
                l = r
                r += 1
        res += calculate(l, r)
        return res