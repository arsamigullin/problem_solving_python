import collections


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1<<i)) for i in range(31))
