import math
from collections import Counter


class Solution:

    def countPairs(self, A, k):
        # n*LogN where N is len of array A
        cnt = Counter(math.gcd(a, k) for a in A)
        res = 0
        # d * d where d is number of unique gcd between a and k
        for a in cnt:
            for b in cnt:
                # we do a<=b to avoid duplicates
                # a * b % k is a core check
                if a <= b and a * b % k == 0:
                    # cnt[a] * cnt[b] because of multiplication Combinatoric principle, A and B represent different sets
                    # so to find total number of pair is A x B

                    # cnt[a] * (cnt[a] - 1) // 2 is for the items in the same set
                    # to get unique pairs in the same set is n(n-1)//2
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[a] - 1) // 2
        # Time complexity N*LogN + d^2
        return res
