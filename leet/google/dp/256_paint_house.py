from typing import List

# # similar 256, 265, 931, 1289
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        d = [[-1] * 3 for _ in range(len(costs))]

        def helper(i, prevColor):
            if i >= len(costs):
                return 0
            _min = float('inf')
            for j, colorCost in enumerate(costs[i]):
                if j == prevColor:
                    continue
                if d[i][j] == -1:
                    d[i][j] = colorCost + helper(i + 1, j)

                _min = min(_min, d[i][j])
            return _min

        return helper(0, -1)

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        dp = [[0]*len(costs[0]) for _ in range(len(costs))]
        for i in reversed(range(len(costs)-1)):
            for k in range(len(costs[0])):
                costs[i][k] += min([costs[i+1][j] for j in range(len(costs[0])) if j!=k])
        return min(costs[0])


if __name__ == '__main__':
    s = Solution()
    s.minCost([[5, 8, 6], [19, 14, 13], [7, 5, 12], [14, 15, 17], [3, 20, 10]])
