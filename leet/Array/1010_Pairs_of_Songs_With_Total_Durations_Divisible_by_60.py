import collections
import math
from typing import List

class Solution:
    '''
    the solution is based to the following
    (a+b)%60 = (a%60 + b%60)%60 = (70 + 80)%60 = (70%60+80%60)%60 = 30
    here, if we remove the most right modulo operation (a%60 + b%60)%60 we will get
    a%60 + b%60 = 60
    Meaning if modulos of two numbers a and b result in 60, the sum a and b numbers divisible by 60 as well
    '''
    def numPairsDivisibleBy60(self, A):
        rep = collections.defaultdict(int)
        count = 0
        for t in A:
            if t%60 == 0:
                count += rep[t%60]
            else:
                count += rep[60-t%60]
            rep[t%60]+=1
        return count

if __name__ == '__main__':
    s = Solution()
    s.numPairsDivisibleBy60([60, 60, 60,60])
    s.numPairsDivisibleBy60([60,60,60])
    s.numPairsDivisibleBy60([30,20,150,100,40])