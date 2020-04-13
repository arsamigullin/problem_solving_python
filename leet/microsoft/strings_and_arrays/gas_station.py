import typing
List = typing.List
# https://leetcode.com/problems/gas-station/



class Solution:
    '''
    the idea is if after passing the whole array total_tank is greater or equal 0, it is possible 
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_tank = 0
        current_tank = 0
        j = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total_tank += g - c
            current_tank += g - c
            if current_tank < 0:
                current_tank = 0
                j = i + 1
        return j if total_tank >= 0 else -1

        return starting_station if total_tank >= 0 else -1


if __name__ == "__main__":
    s = Solution()
    s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])