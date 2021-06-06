import collections
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:

        d = collections.defaultdict(int)
        get_ind = lambda ch: ord(ch) - ord('a')

        # precompute bitmasks for every word
        for w in words:
            bitmask = 0
            for ch in w:
                bitmask |= 1 << get_ind(ch)
            # since we need to maximize the product
            # we want to store the max length
            d[bitmask] = max(d[bitmask], len(w))

        max_prod = 0
        for x in d:
            for y in d:
                # this means there is no common letters in words
                # represented by x and y bitmasks
                if x & y == 0:
                    # and we do maximize the product
                    max_prod = max(max_prod, d[x] * d[y])
        return max_prod
