import heapq
from _heapq import heappop
from heapq import heappush
from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        m = len(mat[0])
        heap = [(sum(r[0] for r in mat),[0]*n,0)]
        for _ in range(k):
            _sum, pointers, row_idx = heapq.heappop(heap)
            for i in range(row_idx, n):
                j = pointers[i]
                if j == m-1:
                    continue
                new_pointers = pointers[:]
                new_pointers[i]+=1
                val = _sum-mat[i][j]+mat[i][j+1]
                heapq.heappush(heap,(val, new_pointers, i))
        return _sum

from heapq import heappush, heappop

# [1,10,10]
# [1,4,5]
# [2,3,6]
# pointers is array of length n where pointers[i] is jth index used on row i. The val is determined by the
# pointers, for example we did val, pointers, row_idx = heappop(heap) where pointers = [1,2,1],
# that means the val is a sum mat[0][1]+mat[1][2]+mat[2][1]
# O(n*k*logk) where n is number of rows
class Solution2:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = len(mat)
        col = len(mat[0])

        heap = [(sum(r[0] for r in mat), [0] * row, 0)]
        for _ in range(k):
            val, pointers, row_idx = heappop(heap)
            for i in range(row_idx, row):
                j = pointers[i]
                if j == col - 1:
                    continue

                new_pointers = pointers[::]
                new_pointers[i] += 1
                new_val = val - mat[i][j] + mat[i][j + 1]
                heappush(heap, (new_val, new_pointers, i))
        return val

class Solution:

    def kthSmallest(self, mat: List[List[int]], k: int) -> int:

        ans = []
        h = [[0, -1, 0]]
        row_counts = {i-1:0 for i in range(len(mat)+1)}

        while h:

            cost, i, j = heappop(h)
            if row_counts[i] >= k: continue
            row_counts[i] += 1

            if i + 1 == len(mat):
                ans.append(cost)
                if len(ans) == k: return cost
                continue

            for idx, val in enumerate(mat[i+1]):
                heappush(h, [cost + val, i + 1, idx])

class Solution1:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        if m == 1: return mat[0][k - 1]

        ans = self.kSmallestSumPairs(mat[0], mat[1], k)
        for r in range(2, m):
            ans = self.kSmallestSumPairs(ans, mat[r], k)
        return ans[k - 1]

    def kSmallestSumPairs(self, arr1, arr2, k):  # Return up to `k` smallest sum of pairs of `arr1` and `arr2`
        minHeap = []
        for c in range(min(len(arr1), k)):
            heappush(minHeap, (arr1[c] + arr2[0], c, 0))

        ans = []
        while k > 0 and minHeap:
            _sum, c1, c2 = heappop(minHeap)
            ans.append(_sum)
            if c2 + 1 < len(arr2):
                heappush(minHeap, (arr1[c1] + arr2[c2 + 1], c1, c2 + 1))
            k -= 1
        return ans

if __name__ == '__main__':
    s = Solution2()
    s.kthSmallest([[1,10,10],[1,4,5],[2,3,6]], 7)
    s.kthSmallest([[1,3,11],[2,4,6]], 5)