import collections
from typing import List


class Solution1:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:

        if len(words1) != len(words2):
            return False

        d = collections.defaultdict(set)
        for a, b in pairs:
            d[a].add(b)
            d[b].add(a)

        for u, v in zip(words1, words2):
            if u == v:
                continue
            if v not in d[u] and u not in d[v]:
                return False
        return True


class Solution2(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        pairset = set(map(tuple, pairs))
        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset
                   for w1, w2 in zip(words1, words2))