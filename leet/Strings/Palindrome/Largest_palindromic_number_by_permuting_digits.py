# microsoft
import collections
from collections import Counter


class Solution:
    def solve(self, s):
        ch_count = sorted(Counter(s).items(), reverse=True)
        mid = ''
        res = []
        for num, cnt in ch_count:
            if cnt % 2 == 1 and not mid:
                mid = num
            if num == '0' and len(res) == 0:
                continue
            if cnt > 1:
                res.append(num * (cnt // 2))
        r = ''.join(res) + mid + ''.join(reversed(res))
        print(r if r else 0)
        return r if r else 0

    def repeat(self, A):
        c = collections.Counter(A)
        # at most 1 char with an odd count
        digits = sorted(c.keys(), reverse=True)
        mid = ''
        res = []
        # abba
        # cabac
        for digit in digits:
            if c[digit] % 2 == 1 and not mid:
                mid = digit
            if digit == '0' and len(res) == 0:
                continue
            if c[digit] > 1:
                res.append(digit * c[digit]//2)

        palindrome = ''.join(res) + mid + ''.join(res[::-1])
        return palindrome

if __name__ == '__main__':
    s = Solution()
    s.solve("8199")
    s.solve("11111900000")
    s.solve("9998855661122")
    s.solve("7002")
    s.solve("313551")
    s.solve("010001")
    s.solve("313566651")
    s.solve("54321")
    s.solve('0000')
    s.solve("39878")
    s.solve("00900")
    s.solve("3492834102438729")
