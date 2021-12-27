from typing import List


def bisect_left(arr, targ):
    lo = 0
    hi = len(arr)
    while lo<hi:
        mid = lo + (hi-lo)//2
        if arr[mid]<targ:
            lo = mid + 1
        else:
            hi = mid
    return lo

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)

if __name__ == '__main__':
    s = Solution()
    s.lengthOfLIS([5,6,1,3,8,1])
