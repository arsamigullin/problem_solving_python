import collections
from bisect import bisect


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)




class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.limit = 300
        self.arr = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.limit < timestamp:
            index = bisect.bisect_right(self.arr, timestamp - 300)
            self.arr = self.arr[index:]
            self.limit = timestamp
        return len(self.arr)
