# Algo
# 1. split start and and times and sort them
# 2. iterate over start times and see if it is greater or equal to the end time
#    if it is, this means a single one meeting with that end time has ended that is why we
#    subtracting 1 (freeing up room)
# 3. Complexity NlogN
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start_timing = [timeset[0] for timeset in intervals]
        end_timing = [timeset[1] for timeset in intervals]
        start_timing.sort()
        end_timing.sort()
        sp = 0
        ep = 0
        room_cnt = 0
        while sp < len(start_timing):
            if start_timing[sp] >= end_timing[ep]:
                room_cnt -= 1
                ep+=1
            room_cnt += 1
            sp+=1
        return room_cnt