import collections
import heapq


class StockPrice:

    def __init__(self):
        self.ts = collections.defaultdict(int)
        self.min_heap = []
        self.max_heap = []
        self.last_ts = 0

    def update(self, timestamp: int, price: int) -> None:
        self.ts[timestamp] = price # this ensures we always have valid price under timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))
        self.last_ts = max(self.last_ts, timestamp)

    def current(self) -> int:
        return self.ts[self.last_ts]

    def maximum(self) -> int:
        while self.ts[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)

        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.ts[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)

        return self.min_heap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()