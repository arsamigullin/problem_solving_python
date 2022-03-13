# microsoft
# Given an integer(+ve or -ve) consisting of at least one 5 in its digits(can have more than one 5). Return the maximum value by deleting exactly one 5 from its digit.
# Ex: N = 1598 => result = 198(remove the only 5 from the sequence)
# N = 150,958 => result = 15,098(we wanna return the maximum value 15,098 > 10,958)
# N = -5859 => result = -589 ( -589>- 859)
import math


class Solution:
    def solve(self, s):
        start = 1 if s[0] == '-' else 0
        max_num = -math.inf
        for i in range(start, len(s)):
            if s[i] == '5':
                num = int(s[:i]+s[i+1:])
                max_num = max(max_num, num)
        return max_num

if __name__ == '__main__':
    s= Solution()
    s.solve("-5123555")

