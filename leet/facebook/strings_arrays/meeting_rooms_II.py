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
            # if this condition true
            # that means we can use the room was used before (because it is free now)
            if start_timing[sp] >= end_timing[ep]:
                room_cnt -= 1
                ep += 1
            # otherwise we want to increase count of used rooms
            room_cnt += 1
            sp += 1
        return room_cnt


class Solution:
    def minMeetingRooms(self, intervals) -> int:

        # 0, 5, 15
        # 10, 15, 30
        starts = sorted([s for s, _ in intervals])
        ends = sorted([e for _, e in intervals])
        # NOTE: there is not relationship between starts and ends after sorting
        # meaning starts[i] and ends[i] are not necessarily belong to the same meeting
        n = len(intervals)
        s, e = 0, 0
        used_rooms = 0
        for i in range(n):
            # if srtart[s] is >= ends[e] that means one of the going meetings ended
            if starts[s] >= ends[e]:
                e += 1
                used_rooms -= 1 # realease the room

            # the room are taken anyway
            used_rooms += 1
            s += 1
        return used_rooms


if __name__ == '__main__':
    s = Solution()
    s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
