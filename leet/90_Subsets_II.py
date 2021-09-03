from typing import List

#O(n*2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def helper(i, subs):
            result.append(subs[:])

            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j - 1]:
                    continue
                subs.append(nums[j])
                helper(j + 1, subs)
                subs.pop()

        helper(0, [])

        return result