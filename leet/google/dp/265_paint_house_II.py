from typing import List
# # similar 256, 265, 931, 1289
#O(nk^2)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        for house in reversed(range(len(costs) - 1)):
            for color in range(len(costs[0])):
                # for each cost of potential color of the house we adding the min value
                # of potential color of the next house (and when doing that we exclude current cost j!=
                costs[house][color] += min(
                    [costs[house + 1][nextHouseColor] for nextHouseColor in range(len(costs[0])) if
                     nextHouseColor != color])
        return min(costs[0])


# O(n)
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        k = len(costs[0])
        # each house can be potentially painted into one of the k colors
        # painting cost is costs[house][color]
        # for each house
        for house in range(1, len(costs)):
            # we do find two minimum values gotten from painting cost of previous house
            # this helps us to reduce complexity substantially
            # that is instead of finding min cost iterating over all potential colors of the previous hose
            # we find two min values
            # first_min<=second_min always
            first_min = second_min = None
            for color in range(k):
                cost = costs[house - 1][color]
                if first_min is None or cost < costs[house - 1][first_min]:
                    second_min = first_min
                    first_min = color
                elif second_min is None or cost < costs[house - 1][second_min]:
                    second_min = color
            # Having found two min values
            # we add up them to the appropriate costs of the current values
            # NOTE: if we met the color that is equal to the first_min color
            # we use second_min color for the costs
            for color in range(k):
                if color == first_min:
                    costs[house][color] += costs[house - 1][second_min]
                else:
                    costs[house][color] += costs[house - 1][first_min]

        return min(costs[-1])