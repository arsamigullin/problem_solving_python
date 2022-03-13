from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        diffs = {}
        for item in arr:
            if item - difference in diffs:
                diffs[item] = diffs[item - difference] + 1
            else:
                diffs[item] = 1
        return max(diffs.values())