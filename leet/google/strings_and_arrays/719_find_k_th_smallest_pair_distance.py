from typing import List


# O(NlogN + NlogW)
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        '''
        The function possible returns True if count of pairs with distances less or equal our guess is greater or equal k.
        In other words, if it returned True it means there are at least k pairs with distances less or equal guess.

        :param nums:
        :param k:
        :return:
        '''

        def possible(guess):
            count = l = 0
            for r, val in enumerate(nums):
                # we reduce window by increasing l pointer
                # if the distance of pairs is greater than guess
                while nums[r] - nums[l] > guess:
                    l += 1
                # NOTE: this is count of pairs with distance less than guess
                count += r - l
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]  # this W
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
