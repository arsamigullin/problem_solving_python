# the two pointer approach
# Initially two pointers are set at the same position
# once the range is broken we add the result to the list
# and we see if prev i item is equal j-1. If so it means the range consists of 1 element
# in case of difference between them we add range with ->
# since the latest element will not be handled, we do it after loop
class Solution:
    def summaryRanges(self, nums: list) -> list:
        if not nums:
            return []

        i, j = 0, 0
        res = []
        d = 0

        def add_interval():
            if nums[i] == nums[j - 1]:
                res.append(str(nums[i]))
            else:
                res.append(f"{nums[i]}->{nums[j - 1]}")

        while j < len(nums):
            if nums[j] - nums[i] != d:
                d = 0
                add_interval()
                i = j
            else:
                d += 1
                j += 1

        add_interval()
        return res