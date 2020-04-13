class SolutionMy:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and list(bin(n)).count('1') == 1


class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

#How to get / isolate the rightmost 1-bit : x & (-x)
# we isolate the rightmost bit and see if this is the only bit in bit string (i.e. if n & (-n) == n)
# n & (-n) is a way to keep the rightmost 1-bit and to set all the other bits to 0.
# 7 & (-7) = 7 & (invert all bits of 7 + 1)= 0000111 & (1111000 + 1) = 0000111 & 1111001 = 0000001
# 7 !=1

# 16 & (-16) = 16 & (invert all bits of 16 + 1) = 00010000 & (11101111 + 1) = 00010000 & 11110000 = 00010000
# 16 == 16
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n

#  x & (x - 1) is a way to set the rightmost 1-bit to zero.
# To subtract 1 means to change the rightmost 1-bit to 0 and to set all the lower bits to 1.
# if x & (x - 1) == 0 the number is power of two
# 4 & (4-1) = 00100 & (00100 - 1) = 00100 & 00011 = 0
# 4 is power of 2
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (n - 1) == 0