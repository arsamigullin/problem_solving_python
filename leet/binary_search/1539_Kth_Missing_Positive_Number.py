from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        let's compare the input array [2, 3, 4, 7, 11] with an array with no missing integers: [1, 2, 3, 4, 5]
        Before 2, there is 2 - 1 = 1 missing integer.
        Before 3, there is 3 - 2 = 1 missing integer.
        Before 4, there is 4 - 3 = 1 missing integer.
        Before 7, there are 7 - 4 = 3 missing integers.
        Before 11, there are 11 - 5 = 6 missing integers.
        We can notice the difference forms also sorted array
        # The number of positive integers which are missing before the arr[idx] is equal to arr[idx] - idx - 1.
        '''
        lo = 0
        hi = len(arr)
        while lo < hi:
            # The number of positive integers which are missing before the arr[idx] is equal to arr[idx] - idx - 1.
            mid = lo + (hi - lo) // 2
            if arr[mid] - mid - 1 < k:
                lo = mid + 1
            else:
                hi = mid
        return lo + k


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k