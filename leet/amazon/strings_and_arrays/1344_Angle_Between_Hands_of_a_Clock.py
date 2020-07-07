class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        360 degree / 12 = 30
        5 mins is 30 deg, 10 mins is 60 deg and so on
        Every 12 mins hour arrow moves one point
        '''
        if hour == 12:
            hour = 0
        hrsdeg = (hour * 30) + (minutes * 6) / 12
        mindeg = (minutes * 30) / 5
        # print(hrsdeg - mindeg, mindeg - hrsdeg)
        diff = abs(hrsdeg - mindeg)
        return min(diff, 360 - diff)
