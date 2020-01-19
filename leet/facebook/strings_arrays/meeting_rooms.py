# Algo
# 1. sort intervals by end_time and check for overlaps
class Solution:
    def canAttendMeetings(self, intervals: list) -> bool:
        intervals.sort(key=lambda x: x[1])
        # pass
        for i in range(len(intervals) - 1):
            s_curr, e_curr = intervals[i]
            s_prev, e_prev = intervals[i + 1]
            if s_curr >= e_prev or e_curr <= s_prev:
                continue
            else:
                return False
        return True
