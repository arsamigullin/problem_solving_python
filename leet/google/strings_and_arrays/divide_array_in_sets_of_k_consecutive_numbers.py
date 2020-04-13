import collections
import typing
List = typing.List

# this problem
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

# similar problem split_array_into_consecutive_subsequences.py
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = collections.Counter(nums)
        nums.sort() # this must have
        for x in nums:
            if count[x] == 0:
                continue
            for i in range(1, k):
                if count[x + i] > 0:
                    count[x + i] -= 1
                # if no numbers left, this means we cannot compose sequence
                else:
                    return False
            count[x] -= 1
        return True
