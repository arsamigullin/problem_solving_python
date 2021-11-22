import collections
from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0] * (len(w)+1)
        for i in range(len(w)):
            self.prefix[i+1] = self.prefix[i] + w[i]
        #print(self.prefix)
        self.prefix = self.prefix[1:]
        self.total = self.prefix[-1]
        self.d = collections.defaultdict(int)
        self.nums = collections.defaultdict(int)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        self.nums[int(target)]+=1
        lo = 0
        hi = len(self.prefix)
        while lo < hi:
            mid = (lo + hi)//2
            if self.prefix[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        self.d[lo]+=1
        return lo

    def printd(self):

        print(self.d)
        print(self.nums)

if __name__ == '__main__':
    s = Solution([1,2,3,4,3])
    for i in range(10000):
        s.pickIndex()

    s.printd()