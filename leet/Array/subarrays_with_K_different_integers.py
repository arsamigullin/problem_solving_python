import collections
import typing
List = typing.List

# This problem
# https://leetcode.com/problems/subarrays-with-k-different-integers/

# exact problem
#number_of_substrings_containing_all_three_characters.py

class Solution:
    '''
    Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good
    if the number of different integers in that subarray is exactly K.

    We need to count contiguous subbarrays with exact K distinct numbers, for example
    112 contains two distinct subarrays 12 and 112

    '''
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        res = 0

        first_unique, left = 0, 0
        freq = collections.defaultdict(int)

        for c in A:
            freq[c] += 1

            # this part is easy to understand.
            # Once the count of unique number are greater K we remove the most left item of the subarray
            # and define the left boundary of the subarray first_unique = left
            if len(freq) > K:
                del freq[A[left]]
                left += 1
                first_unique = left

            # to understand how works this part let's consider an example:
            # [1,1,2,1,3]
            # Once we reached index 2 the freq dictionary looks like this
            # freq = {1:2, 2:1}
            # to count how many contiguous subbarrays has K unique numbers
            # we do the following
            # left is 0
            # A[left] is 1
            # freq[A[left]] is 2
            # 1 iteration:
            # Node: A[left], i.e. A[0] is 1
            # we decrease freq[A[left]] and increase left
            # freq[1] is 1
            # left is 1
            # 2 iteration:
            # # Node: A[left], i.e. A[1] is again one 1
            # but count freq[1] is 1 (not greater 1), so we stop

            # So, we move the left pointer to the right passing the duplicates of 1
            # COUNT OF DUPLICATES (left - first_unique + 1) will equal the count of contiguous subbarrays
            # involving only the elements of that range [first_unique: left]

            # Once we reach the index 3
            # freq = {1:2, 2:1}
            # we will decrease count of 1 and move left pointer further to the right, expanding the range
            # We already have contiguous subbarrays counted within range [0:2]
            # to this result we add the count of contiguous subbarrays of [0:3]
            # 0 is first_unique because we never exceeded K so far
            # 3 because we increased the last value of left pointer (which was 2)

            # When expanding the range we need to count contiguous subbarrays that involves added items

            if len(freq) == K:
                while freq[A[left]] > 1:
                    freq[A[left]] -= 1
                    left += 1
                res += left - first_unique + 1

        return res

if __name__ == "__main__":
    s = Solution()
    #print(s.subarraysWithKDistinct([1,2,1,3,4],3))
    print(s.subarraysWithKDistinct([1,1,1,2,1,2,3],2))