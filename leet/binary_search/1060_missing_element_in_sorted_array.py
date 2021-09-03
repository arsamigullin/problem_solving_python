from typing import List
# binary_search

class Solution1:
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


class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:

        # how many missing numbers before nums[i]
        # this formula is straightforward
        # when doing nums[i] - nums[0] we define the delta between the first item and the item under i
        # BUT some numbers could be existed between nums[0] and nums[i], and not to count them we subtract index
        # [4,7,9,10]
        # let's consider 9 with its index 2
        # nums[2] - nums[0] - 2 = 9-4-2 = 3
        # Doing 9-4-1 we would get the missing nums if 7 did not exist
        # Since there is also 7 we must subtract the 9th index
        missing = lambda i: nums[i] - nums[0] - i
        n = len(nums)
        if k > missing(n - 1):
            return nums[n - 1] + k - missing(n - 1)

        lo = 0
        hi = n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if k > missing(mid):
                lo = mid + 1
            else:
                hi = mid

        return nums[lo - 1] + k - missing(lo - 1)




class Solution3:
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

if __name__ == '__main__':
    arr = [4, 7, 9, 10]
    k = 3
    s = Solution2()
    s.missingElement(arr, k)