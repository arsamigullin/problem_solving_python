import collections
from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        memo = collections.defaultdict(int)

        def dp(i, j, k):
            if k == 1:
                # if one mailbox left
                # we put it to the middle (i+j)//2
                # and then we need to sum distance between the middle and every house
                # in short, instead of doing houses[mid] -houses[i] and houses[j] - houses[mid]
                # we do houses[j] - houses[i] because it is the same
                total_distance = 0
                while i < j:
                    total_distance += houses[j] - houses[i]
                    i += 1
                    j -= 1
                return total_distance
            if (i, j, k) not in memo:
                memo[(i, j, k)] = float('inf')
                for m in range(i + k - 2, j): # i + k - 2 somehow reduces runtime
                #for m in range(i, j):
                    memo[(i, j, k)] = min(dp(i, m, k - 1) + dp(m + 1, j, 1), memo[(i, j, k)])
            return memo[(i, j, k)]

        return dp(0, len(houses) - 1, k)

if __name__ == '__main__':
    s = Solution()
    s.minDistance([1,4,8,10,20], 3)