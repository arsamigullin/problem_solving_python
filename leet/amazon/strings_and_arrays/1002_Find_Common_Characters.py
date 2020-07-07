from typing import List


class SolutionMy:
    def commonChars(self, A: List[str]) -> List[str]:
        chars = set()
        for l in A:
            chars = chars.union(l)

        counters = [collections.Counter(s) for s in A]

        res = []

        for ch in chars:
            mincnt = float('inf')
            for counter in counters:
                if counter[ch] == 0:
                    break
                mincnt = min(mincnt, counter[ch])
                counter[ch] -= mincnt
            else:
                res.extend(list(ch * mincnt))
        return res



# this is very fast solution

import collections


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counter = collections.Counter(A[0])
        for w in A[1:]:
            counter &= collections.Counter(w)

        return list(counter.elements())