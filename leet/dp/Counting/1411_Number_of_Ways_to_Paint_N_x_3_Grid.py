
# O(N)
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/574923/JavaC%2B%2BPython-DP-O(1)-Space

# O(lgN)
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/discuss/575485/C++Python-O(logN)-Time

# O(n)


# Explanation from lee215
# Two pattern for each row, 121 and 123.
# 121, the first color same as the third in a row.
# 123, one row has three different colors.
#
# We consider the state of the first row,
# pattern 121: 121, 131, 212, 232, 313, 323.
# pattern 123: 123, 132, 213, 231, 312, 321.
# So we initialize a121 = 6, a123 = 6.
#
# We consider the next possible for each pattern:
# Patter 121 can be followed by: 212, 213, 232, 312, 313
# Patter 123 can be followed by: 212, 231, 312, 232
#
# 121 => three 121, two 123
# 123 => two 121, two 123
#
# So we can write this dynamic programming transform equation:
# b121 = a121 * 3 + a123 * 2
# b123 = a121 * 2 + a123 * 2
#
# We calculate the result iteratively
# and finally return the sum of both pattern a121 + a123
class Solution:
    def numOfWays(self, n: int) -> int:
        w123 = 6
        w121 = 6
        M = 10 ** 9 + 7
        # note: here we use n-1 because the first case is the initial one and we need to
        # subtract it
        for _ in range(n - 1):
            w123, w121 = (2 * w123 + 2 * w121) % M, (3 * w121 + 2 * w123) % M
        return (w123 + w121) % M
