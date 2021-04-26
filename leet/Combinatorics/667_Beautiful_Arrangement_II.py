from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        a = list(range(1,n+1))
        p = n-k
        s = a[p:p+k//2]
        f = a[p+k//2:]
        a[p::2] = f[::-1]
        a[p+1::2] = s
        return a