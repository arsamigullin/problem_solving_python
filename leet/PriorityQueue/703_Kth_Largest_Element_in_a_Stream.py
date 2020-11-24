import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        '''
        we keep the heap size within k
        once it is k we add the val and popping the min item, so the  size of the heap is still k
        doing that the first item of the heap will be essentially the k-th largest item
        '''
        if len(self.heap) == self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]


