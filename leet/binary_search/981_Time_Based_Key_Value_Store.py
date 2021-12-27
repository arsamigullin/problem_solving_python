import collections


class TimeMap:

    def __init__(self):
        self.storage = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    # the problem states that the values should be with timestamp_prev <= timestamp
    # bisect_left returns i such that e in arr[:i] < timestamp and e in arr[i:] >= timestamp
    # bisect_right returns i such that e in arr[:i] <= timestamp and e in arr[i:] > timestamp
    # based on that it is better to use here bisect_right
    def get(self, key: str, timestamp: int) -> str:
        if key in self.storage:
            ind = self.binary_search(self.storage[key], timestamp)
            return self.storage[key][ind][0]
        else:
            return None


    def binary_search(self, data, target):
        lo = 0
        hi = len(data)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if data[mid][1] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if lo < len(data) else len(data) - 1