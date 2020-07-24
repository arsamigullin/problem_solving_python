import collections
from math import factorial
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1

        return sum(int(factorial(v) / factorial(2) / factorial(v - 2)) for k, v in d.items() if v > 1)


class Solution:

    # search for duplicate numbers
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # number of good pairs
        repeat = {}
        num = 0

        # for every element in nums
        for v in nums:

            # number of repeated digits
            if v in repeat:

                # count number of pairs based on duplicate values
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]

                # increment the number of counts
                repeat[v] += 1
            # number has not been seen before
            else:
                repeat[v] = 1
        # return
        return num