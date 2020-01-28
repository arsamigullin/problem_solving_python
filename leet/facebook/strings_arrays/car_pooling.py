# Split and sort (passengers and start locations) and (passengers and end locations)
# sort first in asc order and second in descending (we will use it as stack)
# the idea is while start location is greater or equal end location subtract
# the passengers from car (meaning they already arrived and we must subtract them)

class Solution:
    def carPooling(self, trips: list, capacity: int) -> bool:
        start_loc = sorted([[p, s ] for p, s, _ in trips],key=lambda k: k[1])
        end_loc = sorted([[p, e ] for p, _, e in trips],key=lambda k: k[1], reverse=True)

        pas_count = 0
        for p, s in start_loc:
            while end_loc and s >= end_loc[-1][1]:
                pasend, e = end_loc.pop()
                pas_count-=pasend
            pas_count += p
            if pas_count > capacity:
                return False
        return True