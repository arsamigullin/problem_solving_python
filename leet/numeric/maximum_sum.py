# microsoft
# Question1: Given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum.
# if there are not two numbers whose digits have an equal sum, the function should return -1.
# Constraints: N is integer within the range [1, 200000]
# each element of array A is an integer within the range [1, 1000000000]
#
# Example1:
# Input:
# A = [51, 71, 17, 42]
# Output: 93
# Explanation: There are two pairs of numbers whose digits add up to an equal sum: (51, 42) and (17, 71), The first pair sums up  to 93
#
# Example2:
# Input:
# A = [42, 33, 60]
# Output: 102
# Explanation: The digits of all numbers in A add up the same sum, and choosing to add 42 and 60 gives the result 102
#
# Example3:
# Input:
# A = [51, 32, 43]
# Output: -1
# Explanation: All numbers in A have digits that add up to different, unique sums
import collections
import math


class Solution:

    def solve(self, A):
        sum_digits_dict = collections.defaultdict(list)
        max_num = -1
        for i, n in enumerate(A):
            _sum = 0
            num = n
            while num > 0:
                _sum += num % 10
                num //= 10
            if len(sum_digits_dict[_sum]) < 2:
                sum_digits_dict[_sum].append(A[i])
            if len(sum_digits_dict[_sum]) == 2:
                sum_digits_dict[_sum].sort()
                first, second = sum_digits_dict[_sum]
                if n > first:
                    first = n
                elif n > second:
                    second = n
                sum_digits_dict[_sum] = [first, second]
                max_num = max(max_num, sum(sum_digits_dict[_sum]))

        return max_num


if __name__ == '__main__':
    s = Solution()
    s.solve([51, 32, 43])
    s.solve([42, 33, 60])
    s.solve([51, 71, 17, 42])
