import itertools
import math

from collections import Counter
from math import factorial


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        dp = [0] * (len(tiles) + 1)
        dp[0] = 1
        for n in cnt.values():
            for j in range(len(tiles), 0, -1):
                for i in range(min(j, n), 0, -1):
                    dp[j] += dp[j - i] * factorial(j) // (factorial(i) * factorial(j - i))

        return sum(dp) - 1

class Solution2:
    # same idea
    def numTilePossibilities(self, tiles: str) -> int:
        import collections
        cnt = collections.Counter(tiles)

        def DFS(cnt):
            total = 0
            for key in cnt:
                if cnt[key] > 0:
                    total += 1
                    cnt[key] -= 1
                    total += DFS(cnt)
                    cnt[key] += 1
            return total

        return DFS(cnt)

class Solution3:
    def numTilePossibilities(self, tiles: str) -> int:
        per = set()
        for i, ch in enumerate(tiles):
            for j in itertools.permutations(tiles, i+1):
                per.add(''.join(j))
        return len(per)


if __name__ == '__main__':
    s = Solution()
    s.numTilePossibilities("AAABB")
    s.numTilePossibilities("AAB")
    s.numTilePossibilities("AAABB")

# everything below does not work

class Solution4:

    def numTilePossibilities(self, tiles: str) -> int:

        def helper(arr):
            i = len(arr) - 2
            # from the end find the first arr[i] that is
            # less than arr[i+1]
            while i >= 0 and arr[i] > arr[i + 1]:
                i -= 1

            # if i is less than zero
            # this means nubers in reversed order, just reverse them
            if i < 0:
                arr.reverse()
                return

            # starting from the end find first arr[j] that is greater than arr[i]
            j = len(arr) - 1
            while i < j and arr[i] >= arr[j]:
                j -= 1

            # swap numbers under i and j
            arr[i], arr[j] = arr[j], arr[i]
            # reverse numbers between i+1 and end of arr
            arr[i + 1:] = arr[i + 1:][::-1]

        # the total permutation count is

        n = len(tiles)
        per = set()
        for i in range(len(tiles)):
            cuts = list(tiles[i:])
            n = math.factorial(len(cuts))

            for _ in range(n):
                helper(cuts)
                per.add(''.join(cuts[:]))

            # for j in itertools.permutations(tiles, i+1):
            # per.add(''.join(j))
        return len(per)





class Solution5:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        res = set()
        per = set()
        for i, ch in enumerate(tiles):
            cuts = tiles[i:]
            for j in itertools.permutations(tiles, i+1):
                per.add(''.join(j))
            k = 0

            while k < len(cuts):
                cuts = cuts[1:] + cuts[:1]
                j = 0
                inter = set()
                while j < len(cuts):
                    part = cuts[:j]
                    p = j
                    while p < len(cuts):
                        res.add(part + cuts[p])
                        p += 1
                    j += 1
                k += 1
        print(res)
        return len(res)


