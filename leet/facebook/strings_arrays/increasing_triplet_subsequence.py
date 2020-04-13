from typing import List
import collections
import bisect


# this problem
# https://leetcode.com/problems/increasing-triplet-subsequence/
#     300. longest-increasing-subsequence
#     334. increasing-triplet-subsequence
#     354. russian-doll-envelopes
#     646. maximum-length-of-pair-chain
#     673. number-of-longest-increasing-subsequence
#     674. longest-continuous-increasing-subsequence
#     1395. count-number-of-teams

class SolutionMy:
    '''
    bisect.bisect_left
    Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    Given:  [1,4,3]
    lis: [1]-> [1,4]-> [1,3]

    Given: [1,4,3,5,2]
    lis: [1]->[1,4] ->[1,3]->[1,3,5]
    '''

    def increasingTriplet(self, nums: List[int]) -> bool:

        lis = []
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            # if idx equals len(lis) this means that num is greater than all elements in lis
            if idx == len(lis):
                lis.append(num)
            else:
                # otherwise the num is less than all elements in nums
                # OR the same element num was found in lis
                lis[idx] = num
        return len(lis) >= 3

# interesting solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = large = None
        for n in nums:
            if small == None or small >= n:
                small = n
            elif large == None or large >= n:
                large = n
            else:
                return True
        return False


if __name__ == '__main__':
    s = SolutionMy()
    s.increasingTriplet([1,4,3])
    s.increasingTriplet([4, 3, 2, 3, 4])
    s.increasingTriplet([2, 2, 2, 2, 2])
    s.increasingTriplet([1, 2, 3, 4, 5])
