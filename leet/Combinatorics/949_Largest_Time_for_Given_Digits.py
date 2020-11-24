import itertools
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_minutes = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            if 0 <= h1 * 10 + h2 <= 23 and 0 <= m1 * 10 + m2 <= 59:
                mins = h1 * 10 * 60 + h2 * 60
                mins += m1 * 10 + m2
                max_minutes = max(max_minutes, mins)
        hours = str(max_minutes // 60)
        mins = str(max_minutes % 60)

        return "" if max_minutes == -1 else f"{'0' + hours if len(hours) == 1 else hours}:{'0' + mins if len(mins) == 1 else mins}"


if __name__ == '__main__':
    s = Solution()
    s.largestTimeFromDigits([0,3,0,0])

