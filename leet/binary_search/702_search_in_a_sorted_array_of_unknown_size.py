# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = 2147483647
        # while lo<hi:
        #     mid = lo + (hi-lo)//2
        #     if reader.get(mid) == 2147483647:
        #         hi = mid
        #     else:
        #         lo = mid + 1
        lo, hi = 0, 1
        while reader.get(hi) < target:
            lo = hi
            hi = hi * 2  # <<= 1

        # hi = lo
        # lo = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            val = reader.get(mid)
            if reader.get(mid) == target:
                return mid
            elif val > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1