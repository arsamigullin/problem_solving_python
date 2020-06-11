from typing import List

# if current bulb to switch doest no match the the index it at
# and it is greater than current track
# then we update the current track with that maximum
# and once we have i+1 equals track we increase moments
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        track = -1
        momemts = 0
        for i, l in enumerate(light):
            track = max(track, l)
            if track == i + 1:
                momemts+=1
        return momemts

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        track = -1
        momemts = 0
        for i, l in enumerate(light):
            if track == i + 1:
                if l > i + 1:
                    track = l
                else:
                    momemts += 1
                    track = -1
            elif l == i + 1 and track == -1:
                momemts += 1
            elif l > i + 1:
                track = l
        return momemts

if __name__ == '__main__':
    s = Solution()
    s.numTimesAllBlue(
[1,15,3,4,5,6,16,8,9,10,13,12,11,14,2,7,17,18,19])