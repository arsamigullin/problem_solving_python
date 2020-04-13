import typing
List = typing.List

#this problem
# https://leetcode.com/problems/non-overlapping-intervals/
# this problem has been explained in Cormen book
# Instead of finding count of intervals to remove we count non overlaping intervals
# and then subtract it from the total amount of intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda item: item[1])
        curr = float('-inf')
        cnt = 0
        for start, end in intervals:
            if curr <= start:
                curr = end
                cnt += 1
        return len(intervals) - cnt
