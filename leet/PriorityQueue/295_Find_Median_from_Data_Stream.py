from bisect import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
    # O(N + lgN)
    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n%2 == 1:
            return self.arr[n//2]
        else:
            r_ind = n//2
            l_ind = r_ind-1
            return (self.arr[r_ind] + self.arr[l_ind])/2


from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hi = []
        self.lo = []

    # Why do we use negative values in the self.lo?
    # because we want to keep the max value on the top of the queue

    # Why do we use the positive values in the self.hi
    # because we want to keep the max value on the top of the queue

    # len self.hi will always be greater or equal to self.lo
    def addNum(self, num: int) -> None:
        if len(self.hi) == len(self.lo):
            heappush(self.hi, -heappushpop(self.lo, -num))
        else:
            heappush(self.lo, -heappushpop(self.hi, num))

    def findMedian(self) -> float:
        if len(self.hi) == len(self.lo):
            return (self.hi[0] - self.lo[0])/2
        else:
            return self.hi[0]