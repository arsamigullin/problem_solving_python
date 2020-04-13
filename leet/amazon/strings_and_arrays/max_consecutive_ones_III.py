# this problem
# https://leetcode.com/problems/max-consecutive-ones-iii/

# similar problem
#
import collections
import  typing
List = typing.List
class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        i, ans = 0, 0
        cnt = collections.defaultdict(int)
        for j in range(len(nums)):
            # we do count each element in array
            cnt[nums[j]] += 1
            # and check how many of them are not 1's
            # j - i is a total count of elements between j and i indexes
            # j - i - cnt[1] is how many of them are not ones
            if j - i - cnt[1] >= K:
                # since i was pointing to the left boundary of the sliding window
                # we subtract one from count of that element, meaning we no longer count it
                # and narrow sliding window by increasing i
                cnt[nums[i]] -= 1
                i += 1

            if j - i >= ans:
                ans = j - i + 1
        return ans

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]
            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1
        return right - left + 1