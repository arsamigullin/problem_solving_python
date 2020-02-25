import collections
import heapq
# The requirement are to find k most frequent words in O(nlogk) and is if the count the same we have to pick up the word
# in alphabetic order
# In python we can do even better
# comparison in python works with sets
# (1,5)>(1,6) is False

class Solution(object):
    def topKFrequent(self, words, k):
        #O(n)
        count = collections.Counter(words)
        #O(n)
        heap = [(-freq, word) for word, freq in count.items()]
        #O(n)
        heapq.heapify(heap)
        # O(klogn)
        return [heapq.heappop(heap)[1] for _ in range(k)]

if __name__ == "__main__":
    s = Solution()
    s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)