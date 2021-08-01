from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            # even if K is negative, at the end of the running algo it will never less than -1
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1
        return right - left + 1

if __name__ == '__main__':
    s = Solution()
    s.longestOnes([1, 0, 0, 0, 0, 0], 3)
    s.longestOnes([1, 0, 0, 0, 0], 3)
    s.longestOnes([0,0,0,0],3)
    s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)