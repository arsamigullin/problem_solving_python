from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort()

        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i - 1])

        count = 0
        for w in reversed(warehouse):
            if count < len(boxes) and boxes[count] <= w:
                count += 1
        return count
