import heapq
from typing import List

# Complexity O(NlogN)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones) # O(N)
        while len(stones)>1:
            first = heapq.heappop(stones) # O(lgN)
            second = heapq.heappop(stones) # O(lgN)
            smashed = abs(first) - abs(second)
            if smashed != 0:
                heapq.heappush(stones, -smashed) # O(lgN)
        return 0 if len(stones) == 0 else abs(stones[0])

# O(n) solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Set up the bucket array.
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # Bucket sort.
        for weight in stones:
            buckets[weight] += 1

        # Scan through the weights.
        biggest_weight = 0
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight