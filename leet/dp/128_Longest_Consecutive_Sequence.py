from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            '''
            let's say we have an array [4,3,2,1]
            for numbers 4,3,2 the below if would be False
            '''
            if n - 1 not in num_set:
                curr_num = n
                cur_longest = 1

                while curr_num + 1 in num_set:
                    cur_longest += 1
                    curr_num += 1

                longest = max(longest, cur_longest)

        return longest