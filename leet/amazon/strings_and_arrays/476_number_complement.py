from math import log2, floor

class Solution:
    def findComplement(self, num):
        l = len(bin(num)[2:]) # this is the same as floor(log2(num)) + 1
        res = sum(2**i for i in range(l)) # this is the same as bitmask = (1 << l) - 1
        return num^res

from math import log2
class Solution:
    def findComplement(self, num):
        # n is a length of num in binary representation
        n = floor(log2(num)) + 1
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # flip all bits
        return bitmask ^ num


# fliping by bit
class Solution:
    def findComplement(self, num):
        todo, bit = num, 1
        while todo:
            # flip current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return num


class Solution:
    def findComplement(self, num):
        # bitmask has the same length as num and contains only ones 1...1
        bitmask = num
        bitmask |= (bitmask >> 1)
        bitmask |= (bitmask >> 2)
        bitmask |= (bitmask >> 4)
        bitmask |= (bitmask >> 8)
        bitmask |= (bitmask >> 16)
        # flip all bits
        return bitmask ^ num