import collections
import math
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        def backtrack(i, arr):
            if i == len(arr):
                return 0
            if not arr[i]:
                return backtrack(i +1 , arr)
            min_tx = math.inf
            for j in range(i+1, len(arr)):
                if arr[i]*arr[j] < 0:
                    arr[j]+=arr[i]
                    min_tx = min(min_tx, backtrack(i+1,arr)+1)
                    arr[j] -= arr[i]
            return min_tx



        d = collections.defaultdict(int)
        for a,b,m in transactions:
            d[a]-=m
            d[b]+=m

        return backtrack(0, list(d.values()))

if __name__ == '__main__':
    s = Solution()
    s.minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]])