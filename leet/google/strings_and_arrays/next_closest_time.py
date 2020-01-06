# 1. Convert time into minutes
# 2. Every loop increase the time to 1 minute
# 3. Check if the all letters in allowed
#   We do this with two steps
#   a. Convert minutes to back to hours using divmod func
#       for example divmod(1437,60) is 23 and 57
#       then we do divmod(23,10) which is 2 and 3
#       and then divmod(57,10) which is 5, 7
# all func check if all the numbers are in allowed
# if it is, return the answer

class Solution(object):
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60) # this ensures the time staying within 0-24 range
            #for block in divmod(cur, 60):
                #for digit in divmod(block, 10):
                    #print(digit in allowed)

            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

import  itertools
class Solution(object):
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))

if __name__ == "__main__":
    s = Solution()
    s.nextClosestTime("23:54")