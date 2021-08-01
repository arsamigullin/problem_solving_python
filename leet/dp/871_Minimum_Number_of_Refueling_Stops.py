import heapq
from typing import List
import bisect


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target, float('inf')))
        heap = []
        tank = startFuel
        prev_location = 0
        ans = 0

        for location, cap in stations:
            # Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.
            # that is why we have to subtract the current location from prev one
            tank -= location - prev_location
            # if tank is negative, that means the fuel is not sufficient to reach the next location
            # and we refuel it until the tank is not empty
            # since this is pq, we always will refill with the max amount of fuel
            while heap and tank < 0:
                tank+= -heapq.heappop(heap)
                ans+=1
            if tank < 0: return -1
            heapq.heappush(heap, -cap)
            prev_location = location
        return ans


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t]>=location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)


        for key, distance in enumerate(dp):
            if distance>=target:
                return key
        return -1





if __name__ == '__main__':
    s = Solution()
    s.minRefuelStops(100,10,[[9,60],[20,30],[30,30],[60,40]])
    #target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]