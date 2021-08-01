from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        s=set()
        s.add(stones[0])
        s.add(-stones[0])
        dp=set()
        for i in range(1,len(stones)):
            for j in s:
                dp.add(abs(j-stones[i]))
                dp.add(abs(j+stones[i]))
            s=dp
            dp=set()
        return min(s)


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        tot = sum(stones)
        halfSum = tot//2

        dp = [0] * (halfSum+1)
        for i in range(1, n+1):
            for j in range(halfSum, stones[i-1]):
                dp[j] = max(dp[j], dp[j-stones[i-1]] + stones[i-1])

        return tot - 2 * halfSum


class Solution2:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # https://leetcode.com/problems/last-stone-weight-ii/discuss/294888/JavaC%2B%2BPython-Easy-Knapsacks-DP
        # The post above says this is similar to (or can convert to knapsack question)
        # Divide the numbers into two groups and find the division with smallest difference
        # Between the sums of two groups
        # So we construct the set of all the possible sum of one group
        # And use the sum of all stones to minus the sum of one group, got the sum of another group
        # And then take the global minimum difference out of it
        # Why the smallest left would be the smallest difference? see one comment from above post
        # Suppose we have the smallest difference between two groups
        # And each time, we take A and B from each group, if A > B, we put back A-B
        # And if A < B, we put back B-A, if A == B, we put back nothing.
        # So it equals abs(sum(A)-sum(B))
        dp = {0}
        sumi = sum(stones)
        for i in stones:
            dp |= {s + i for s in dp}
        return min([abs(sumi - i - i) for i in dp])
        # dp = {0}
        # sumi = sum(stones)
        # for s in stones:
        #     dp |= {s+i for i in dp}
        # return min(abs(sumi-i-i) for i in dp)
        # dp = {0}
        # sumi = sum(stones)
        # for s in stones:
        #     dp |= {i+s for i in dp}
        # return min(abs(sumi - i - i) for i in dp)

        # Cannot pass [31,26,33,21,40]


#         heap = []
#         heapq.heapify(heap)
#         for stone in stones:
#             heapq.heappush(heap,-stone)
#         while len(heap)>1:
#             stone1,stone2 = -heapq.heappop(heap),-heapq.heappop(heap)
#             diff = abs(stone1-stone2)
#             if diff == 0:continue
#             else:heapq.heappush(heap,-diff)
#         return -heapq.heappop(heap) if heap else 0


if __name__ == '__main__':
    s = Solution2()
    s.lastStoneWeightII([31,26,33,21,40])