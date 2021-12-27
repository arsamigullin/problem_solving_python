import bisect
import collections

#binary_search
class SnapshotArray1:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = collections.defaultdict(list)
        for i in range(length):
            self.arr[i].append([self.snap_id, 0])

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def bisect_right(self, arr, target_snap_id):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target_snap_id < arr[mid][0]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def snap(self) -> int:
        to_return = self.snap_id
        self.snap_id += 1
        return to_return

    def get(self, index: int, snap_id: int) -> int:
        ind = bisect.bisect_right(self.arr[index], snap_id)
        return self.arr[index][ind - 1][1]


class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        print(self.A[index], [snap_id + 1])
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)