import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        changed.sort()
        if n % 2 == 1:
            return []
        cn = collections.Counter(changed)
        orig = []
        for num in changed:
            if num == 0 and cn[0] > 1:
                cn[num] -= 2
                orig.append(0)
            elif num != 0 and cn[num] and cn[num * 2]:
                orig.append(num)
                cn[num] -= 1
                cn[num * 2] -= 1
        return orig if n // 2 == len(orig) else []

if __name__ == '__main__':
    s = Solution()
    s.findOriginalArray([1,3,4,2,6,8])