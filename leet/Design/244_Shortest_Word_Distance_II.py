import collections
from typing import List

# linear time
class WordDistance:

    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        i, j = 0, 0
        wl1 = self.d[word1]
        wl2 = self.d[word2]
        min_dist = float('inf')
        # when we have two sorted array we always can find
        # the shortest distance btween the elements of these arrays in linear time
        while i < len(wl1) and j < len(wl2):
            min_dist = min(min_dist, abs(wl1[i] - wl2[j]))
            if wl1[i] < wl2[j]:
                i += 1
            else:
                j += 1
        return min_dist

class WordDistance:

    def __init__(self, words: List[str]):
        self.d = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # since we have two arrays sorted we can do binary search
        # we will iterate over smaller array of distances
        if len(self.d[word1])<len(self.d[word2]):
            return self.call(word1, word2)
        else:
            return self.call(word2, word1)

    def call(self, word1, word2):
        min_dist = float('inf')
        for t in self.d[word1]:
            ind2 = self.find(self.d[word2], t)
            diff = abs(ind2 - t)
            min_dist = min(min_dist, diff)
        return min_dist

    # here we do binary search
    def find(self, arr, target):
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if arr[mid] >= target:
                hi = mid - 1
            else:
                lo = mid
        # once we've found lo index
        # we also must to inspect neighbor indexes
        min_ind = lo
        min_diff = abs(arr[lo] - target)
        # to the right
        if 0 <= lo + 1 < len(arr):
            if abs(target - arr[lo + 1]) < min_diff:
                min_diff = abs(target - arr[lo + 1])
                min_ind = lo + 1
        # and to the left
        if 0 <= lo - 1 < len(arr):
            if abs(target - arr[lo - 1]) < min_diff:
                min_ind = lo - 1

        return arr[min_ind]

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)