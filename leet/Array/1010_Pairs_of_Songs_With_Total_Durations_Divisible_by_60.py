import collections
import math
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        pos = [60, 120, 180, 240, 300, 360, 420, 480]

        count = 0
        counter = collections.Counter(time)

        for t in counter:
            if counter[t]==0:
                continue
            for p in pos:
                if abs(t - p) in counter:
                    thesame = 0
                    if abs(t - p) == abs(t):
                        n=abs(counter[t])
                        if n > 2:
                            count+=int(math.factorial(n)/(math.factorial(n-2) * math.factorial(2)))
                        else:
                            count+=n
                    else:
                        count += counter[t] * (counter[abs(t - p)] - thesame)
                    counter[t] = 0
                    counter[abs(t - p)] = 0
        return count

if __name__ == '__main__':
    s = Solution()
    s.numPairsDivisibleBy60([30,20,150,100,40])