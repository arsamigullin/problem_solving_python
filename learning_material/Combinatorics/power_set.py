from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]

        for n in nums:
            subs += [sb + [n] for sb in subs]
        return subs