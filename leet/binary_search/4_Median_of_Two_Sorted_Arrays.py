from typing import List

# median is a mid point of result array after merging two sorted arrays
# a = [7,8,9] b = [-2,-1,0,1,2,3,4]
# after merging [-2,-1,0,1,2,3,4,7,8,9], the len is even so the median is (left_part[-1] + right_part[0])//2 =
# = (2 + 3)//2 = 2.5
# after variable is the middle index after merging a and b arrays
# We will only be dealing with the first "after" items of the array b
# there could be three cases, we assume a array is always smaller or equal to the size of b array
# 1. a[-1] < b[0], here during binary search we tend to move mid closer to b[0]
# 2. a[0] > b[-1], here during binary search we tend to move mid closer to b[-1]
# 3. items intersecting
# all three cases are covered by binary search
# so, the idea is to do binary search on the smaller array and move the mid point of the smaller array
# closer to the point of the larger array so the difference between a[mid] and b[after-mid] is minimal
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0


if __name__ == '__main__':
    s =Solution()
    s.findMedianSortedArrays([7,8,9], [-2,-1,0,1,2,3,4])
    s.findMedianSortedArrays([0,2,3,5,6],[1,6,7,10,11])