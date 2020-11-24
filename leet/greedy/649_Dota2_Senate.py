from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        cnt = 0
        prev = 0
        for i in range(len(timeSeries)):
            cnt += max(0, timeSeries[i] + duration - max(prev, timeSeries[i]))
            if timeSeries[i] + duration >= prev:
                prev = timeSeries[i] + duration

        return cnt