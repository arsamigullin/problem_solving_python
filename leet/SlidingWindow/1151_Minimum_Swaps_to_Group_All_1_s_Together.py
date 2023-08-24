from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)
        i = 0
        j = ones
        ones_in_window = data[:j].count(1)
        count = ones - ones_in_window
        while j < len(data):
            ones_in_window -= data[i]
            ones_in_window += data[j]
            count = min(count, ones - ones_in_window)
            i += 1
            j += 1
        return count


class Solution1:
    def minSwaps(self, data: List[int]) -> int:

        ones = sum(data)
        if ones == len(data):
            return 0
        i = 0
        j = ones
        res = tot = sum(data[:ones])
        while j < len(data):
            tot -= data[i]
            tot += data[j]
            res = max(res, tot)
            j += 1
            i += 1
        return ones - res

