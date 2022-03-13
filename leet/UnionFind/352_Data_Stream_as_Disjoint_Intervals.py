from typing import List

from typing import List


class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.intervals = {}

    def make_set(self, p):
        self.parent.setdefault(p, p)
        self.size.setdefault(p, 1)
        self.intervals.setdefault(p, [p, p])

    def find(self, p):
        if p not in self.parent:
            return None

        rootP = p
        while rootP != self.parent[rootP]:
            rootP = self.parent[rootP]
        while p != rootP:
            newp = self.parent[p]
            self.parent[p] = rootP
            p = newp
        return rootP

    def union(self, u, p):
        rootP = self.find(p)
        rootU = self.find(u)
        if rootP is None or rootU is None:
            return
        if rootP == rootU:
            return

        if self.size[rootP] > self.size[rootU]:
            x = rootU
            y = rootP
            self.parent[rootU] = rootP
            self.size[rootP] += self.size[rootU]
        else:
            x = rootP
            y = rootU
            self.parent[rootP] = rootU
            self.size[rootU] += self.size[rootP]

        x_interval = self.intervals[x]
        del self.intervals[x]

        self.intervals[y] = [min(self.intervals[y][0], x_interval[0]), max(self.intervals[y][1], x_interval[1])]


class SummaryRanges:
    def __init__(self):
        self.dsu = DSU()

    def addNum(self, val: int) -> None:
        '''
        let's assume self.dsu.intervals = [[1,1],[2,2]]
        and now val = 2 came in
        2 is not in DSU yet
        '''
        if val in self.dsu.parent:
            return
        self.dsu.make_set(val)
        # here we try to union 2 and 1
        # and 2 and 3
        # now DSU is
        # 
        self.dsu.union(val, val - 1)
        self.dsu.union(val, val + 1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.dsu.intervals.values())

if __name__ == '__main__':
    s = SummaryRanges()
    s.addNum(1)
    s.getIntervals()
    s.addNum(3)
    s.getIntervals()
    s.addNum(7)
    s.getIntervals()
    s.addNum(2)
    s.getIntervals()
    s.addNum(6)
    s.getIntervals()
