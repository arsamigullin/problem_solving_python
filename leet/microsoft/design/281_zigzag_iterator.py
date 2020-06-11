import itertools
from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0
        self.turn = True

    def next(self) -> int:
        if self.turn:
            if self.i < len(self.v1):
                val = self.v1[self.i]
                self.i += 1
            else:
                val = self.v2[self.j]
                self.j += 1
        else:
            if self.j < len(self.v2):
                val = self.v2[self.j]
                self.j += 1
            else:
                val = self.v1[self.i]
                self.i += 1

        self.turn ^= 1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)

# solution for multiple lists
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = 0
        self.j = 0
        self.l = [v1, v2]
        self.max_len = max([len(arr) for arr in self.l])
        self.prepare_next()

    def prepare_next(self):
        if self.i >= len(self.l):
            self.i = 0
            self.j += 1
        while self.max_len > self.j >= len(self.l[self.i]):
            self.i += 1
            if self.i == len(self.l):
                self.j += 1
                self.i = 0

    def next(self) -> int:
        val = self.l[self.i][self.j]
        self.i += 1
        self.prepare_next()
        return val

    def hasNext(self) -> bool:
        return self.j < self.max_len


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        def vals():
            for i in itertools.count():
                for v in v1, v2:
                    if i < len(v):
                        yield v[i]
        self.vals = vals()
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0