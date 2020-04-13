import heapq
from typing import List




class Solution:
    '''
        consider this example
          1 7 13
        2 1
        4 2
        5

        1 iteration
         0 i=0 j=0 after popping heap
         we push to the heap (9,0,1) and (5,1,0) since j==0
         in heap we have []
         since nums1[0]+nums2[0+1] > nums1[0+1]+nums2[0]
                     2 + 7         > 4 + 1

         (1,0) will be first

         2 iteration
         5 i=1 j=0 after popping heap
         in heap we have [(9,0,1)]
         we push to the heap (11,1,1) and (6,2,0)

         3 iteration
         6 i=2 j=0
         in heap we have [(9,0,1), (11,1,1)]
         we push to the heap (12,2,1) and (_,3,0) - this will not be in heap since 2+1 = len(nums1)

         4 iteration
         9 i=0 j=1
         in heap we have [(11,1,1),(12,2,1)]
         we push to the heap (0,1+1) since j is not 0 we do not add (i+1,0)
         now we add to the heap (15,0,2)

         5 iteration
         11 i=1 j=1
         in heap we have [(12,2,1), (15,0,2)]
         now we push to the heap (17,1,2) since j is not 0 we do not add (i+1,0)

         6 iteration
         12 i=2 j=1
         n heap we have [(15,0,2),(17,1,2)]
         now we push to the heap (18,2,2)

    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def push(i, j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(heap,(nums1[i]+nums2[j], i, j))
        heap = []
        push(0,0)
        pairs = []
        while heap and k>0:
            _, i,j = heapq.heappop(heap)
            print(i,j)
            pairs.append((nums1[i], nums2[j]))
            push(i, j+1)
            if j==0:
                push(i+1,0)
            k-=1
        return pairs

if __name__ == '__main__':
    s = Solution()
    s.kSmallestPairs([2,4,6], [1,7,11],5)