#https://leetcode.com/problems/exam-room/
import collections
import heapq


class ExamRoom1(list):

    def __init__(self, N: int):
        self.N = N

    def seat(self) -> int:
        if not self:
            self.append(0)
            return 0
        else:
            # if student sit at the first place
            dist = 0
            val = 0
            # we do the boundary comparison at the beginning
            # since we need to put the student at lowest seat
            if self[0] != 0:
                dist = self[0]
                val = 0
            # we do finde lowest in the middle
            for i in range(len(self) - 1):
                r = (self[i + 1] - self[i]) // 2
                if r > dist:
                    dist = r
                    val = self[i] + r
            # and only if the end is greater the found distance
            # we do replace it
            if self[-1] != self.N - 1:
                r = self.N - 1 - self[-1]
                if r > dist:
                    dist = r
                    val = self.N - 1

            self.append(val)
            self.sort()
            return val

    def leave(self, p: int) -> None:
        self.remove(p)


class ExamRoom:

    def __init__(self, n: int):
        self.intervals = collections.defaultdict(set)
        self.pq = [(0, 0, n - 1)]
        self.intervals[0].add((0, n - 1))
        self.n = n
        self.zeroDeleted = True
        self.nDeleted = True

    def seat(self) -> int:

        while self.pq:
            dist, i, j = heapq.heappop(self.pq)
            if (i, j) not in self.intervals[i]:
                continue
            break

        if self.zeroDeleted and i == 0:
            self.zeroDeleted = False
            mid = 0
            self.putrigh(mid, j)
        elif self.nDeleted and j == self.n - 1:
            self.nDeleted = False
            mid = self.n - 1
            self.putleft(i, mid)
        else:
            mid = (i + j) // 2
            self.putleft(i, mid)
            self.putrigh(mid, j)

        return mid

    def putleft(self, i, mid):
        heapq.heappush(self.pq, (-((mid - i) // 2), i, mid))
        self.cleanupleft(i, mid)
        self.cleanupright(i, mid)

    def putrigh(self, mid, j):
        heapq.heappush(self.pq, (-((j - mid) // 2), mid, j))
        self.cleanupleft(mid, j)
        self.cleanupright(mid, j)

    def cleanupleft(self, key, y):
        to_evict = set([(i, j) for i, j in self.intervals[key] if i == key])
        self.intervals[key] = self.intervals[key].difference(to_evict)
        self.intervals[key].add((key, y))

    def cleanupright(self, x, key):
        to_evict = set([(i, j) for i, j in self.intervals[key] if j == key])
        self.intervals[key] = self.intervals[key].difference(to_evict)
        self.intervals[key].add((x, key))

    def leave(self, p: int) -> None:
        vals = sorted(self.intervals[p])
        l = vals[0][0]
        r = vals[0][1]
        if p == 0:
            self.zeroDeleted = True
            heapq.heappush(self.pq, (-(r - l), l, r))
            self.cleanupright(p, r)
            self.cleanupleft(p, r)
        elif p == self.n - 1:
            self.nDeleted = True
            heapq.heappush(self.pq, (-(r - l), l, r))
            self.cleanupright(l, p)
            self.cleanupleft(l, p)
        else:
            l = vals[0][0]
            r = vals[1][1]
            self.cleanupleft(l, r)
            self.cleanupright(l, r)
            if (self.zeroDeleted and l == 0) or (self.nDeleted and r == self.n - 1):
                heapq.heappush(self.pq, (-(r - l), l, r))
            else:
                heapq.heappush(self.pq, (-((r - l) // 2), l, r))
            self.intervals.pop(p)

if __name__ == '__main__':
    e = ExamRoom(10)
    e.seat()
    e.seat()
    e.seat()
    e.leave(0)
    e.leave(4)
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.seat()
    e.leave(0)
    e.leave(4)
    e.seat()
    e.seat()
    e.leave(7)
    e.seat()
    e.leave(3)
    e.seat()
    e.leave(3)
    e.seat()
    e.leave(9)
    e.seat()
    e.leave(0)
    e.leave(8)