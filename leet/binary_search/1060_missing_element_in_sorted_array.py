from typing import List
# binary_search

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        # this searches the guess in the original nums array
        def bs(guess):
            if guess > nums[-1]:
                return len(nums) - 1
            lo = 0
            hi = len(nums) - 1
            res = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if guess >= nums[mid]:
                    lo = mid + 1
                    res = mid
                else:
                    hi = mid - 1
            return res

        # here we define the range from which we will pick up the guess
        # this range cannot be greater than nums[-1]+k
        # for example, we have nums = [1,2,3] and k is 3
        # the 3rd missing element is 6 because missing elements starts from 4
        # so they are 4,5,6 and 6 is not greater k+nums[-1]
        # let's call this range search range
        lo = nums[0]
        hi = nums[-1] + k

        while lo <= hi:
            mid = (hi + lo) // 2 # the current guess value in search range
            ind = mid - nums[0] # its index, search range can be started from any number [5,6,7]
            di = bs(mid) # the smallest index that fits guess
            # if the difference between current index of mid(guess) in search range
            # and index in nums equals k, we found this kth missing
            # important thing here is current guess(mid) should not be equal the value
            # nums[di]. if they are equal that means guess(mid) is not missing since it is
            # present in nums
            if ind - di == k and mid != nums[di]:
                return mid
            elif ind - di >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        # how many missing numbers before nums[i]
        missing = lambda i: nums[i] - nums[0] - i
        n = len(nums)
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)

        lo = 0
        hi = n - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            # if the count of missing numbers before index mid is less than k
            # we want to increase lower
            if k > missing(mid):
                lo = mid + 1
            else:
                hi = mid
        return nums[lo - 1] + k - missing(lo - 1)


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1)

        idx = 1
        # find idx such that
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1

        # kth missing number is greater than nums[idx - 1]
        # and less than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)