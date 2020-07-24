import heapq
from typing import List
#heap

class Solution:
    '''

    NOTE: if we found all the sums of the array elements the total number of sums would be n*(n+1)/2
    let's consider an example
    [2, 4, 1, 3] n=4 left=1 right=5

    first we create heap from (val, index).
    [(1,2),(2,0),(3,3),(4,1)]

    1 iteration i = 1
    val = 1, ind = 2
    i>=left we add 1 to res. res = 1

    '''
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(heap)
        res = 0
        for i in range(1, right + 1):
            val, ind = heapq.heappop(heap)
            # if current index is greater than left, i.e. it is in range betwee left and right
            # we add this value to the final result
            if i >= left:
                res += val
            # this check limits the growing heap
            # it adds neighbor value to the right of ind only if
            # it is less than n-1
            if ind < n - 1:
                val += nums[ind + 1]
                heapq.heappush(heap, (val, ind + 1))

        return res


# Naive solution
class Solution1:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]
        arr = []
        for i in range(len(pref)-1):
            for j in range(i+1,len(pref)):
                arr.append(pref[j] - pref[i])
        arr.sort()
        return sum(arr[left-1:right]) % (10**9 + 7)

if __name__ == '__main__':
    s = Solution()
    s.rangeSum([2, 4, 1, 3], 4, 1, 5)
    s.rangeSum([1,2,3,4], 4, 1, 5)