# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#https://docs.python.org/3.8/library/bisect.html
# bisect.bisect locates (but does not insert) the next insertion point to the right of the existing value
# for example [False, False, False, True]. It will return 3
import bisect
class Solution():
    def firstBadVersion(self, n):
        class Wrap:
            def __getitem__(self, i):
                return isBadVersion(i)
        return bisect.bisect(Wrap(), False, 0, n)

class Solution():
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left > right:
            mid = left + (right - left)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
    return left