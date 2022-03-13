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


class HitCounter1:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        i = self.binary_search(timestamp)
        if len(self.hits) == i:
            self.hits.append([timestamp, 1])
        else:
            self.hits[i - 1][1] += 1

    def getHits(self, timestamp: int) -> int:
        i = self.binary_search(timestamp - 300)
        # self.hits = self.hits[i:]
        return sum(h for _, h in self.hits[i:])

    def binary_search(self, target):
        lo = 0
        hi = len(self.hits)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target < self.hits[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return lo


class HitCounter:

    def __init__(self):
        self.hits = collections.deque([])
        self.tot = 0

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])
        self.tot += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits:
            dif = timestamp - self.hits[0][0]
            if dif >= 300:
                self.tot -= self.hits.popleft()[1]
            else:
                break
        return self.tot