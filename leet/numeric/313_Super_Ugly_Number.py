from heapq import heappop, heappush
from typing import List


class SolutionLikeUgly_II:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        heap = [1]
        seen = set()
        for i in range(1, n + 1):
            cur_ugly = heappop(heap)
            for k in primes:
                ugly = k * cur_ugly
                if ugly not in seen:
                    seen.add(ugly)
                    heappush(heap, ugly)
        return cur_ugly



# @lc app=leetcode id=313 lang=python3

from typing import List

from heapq import heappush, heappop

"""
[2, 3, 7]

1: 2, 3, 7
2: 2, 3, 7
3: 3, 7
7, 7
2 * 2: 2, 3, 7
2 * 3: 3, 7
2 * 7: 7
3 * 3: 3, 7
3 * 7: 7
…
"""


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        primes_n = len(primes)
        q = [(primes[0], 1, 0)]
        x = 1
        for _ in range(n - 1):
            x, row, col = heappop(q)

            col_1 = col + 1
            if col_1 < primes_n:
                heappush(q, (row * primes[col_1], row, col_1))

            heappush(q, (x * primes[col], x, col))

        return x


def t(n, primes):
    """
    >>> t(12, [2,7,13,19])
    32
    >>> t(4, [2])
    8
    >>> t(25, [3,5,7,17,19,23,29,43,47,53])
    81
    >>> t(35, [2,3,11,13,17,23,29,31,37,47])
    62
    """
    return Solution().nthSuperUglyNumber(n, primes)

if __name__ == '__main__':
    s = Solution()
    s.nthSuperUglyNumber(12, [2,7,13,19])