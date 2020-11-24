from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted([(s, i) for i, (s, e) in enumerate(intervals)])
        print(starts)

        def binary_search(t, arr):
            lo = 0
            hi = len(arr) - 1

            while lo < hi:
                mid = lo + (hi - lo) // 2
                mid_val, _ = arr[mid]
                if mid_val < t:
                    lo = mid + 1
                else:
                    hi = mid

            val, ind = arr[lo]

            return ind if val >= t else -1

        res = []
        for s, e in intervals:
            res.append(binary_search(e, starts))

        return res

if __name__ == '__main__':
    s = Solution()
    s.findRightInterval([ [3,4], [2,3], [1,2] ])
