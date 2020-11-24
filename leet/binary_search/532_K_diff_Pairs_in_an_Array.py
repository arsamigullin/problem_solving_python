from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        visited = set()
        sorted_nums = sorted([(val, i ) for i, val in enumerate(nums)])
        m = len(nums)
        cnt = 0

        def binary_search(target, j):

            lo = 0
            hi = len(sorted_nums)

            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if mid >= m:
                    return False
                val, ind = sorted_nums[mid]
                if target == val:
                    if ind == j:
                        if (mid + 1 < m and sorted_nums[mid + 1] == target) or (
                                mid - 1 >= 0 and sorted_nums[mid - 1] == target):
                            return True
                        else:
                            return False
                    else:
                        return True
                elif target < val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False

        for n, i in sorted_nums:
            if n in visited:
                continue
            val = k+ n
            if n > k:
                val = n - k
            if binary_search(val, i):
                cnt+=1
                visited.add(n)
                #visited.add(val)
        return cnt

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # nums[right] - nums[left] > k
                # List item 3 in the text
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result

from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result

if __name__ == '__main__':
    s  =Solution()
    s.findPairs([-1,-2,-3], 1)
    s.findPairs([3,1,4,1,5], 2)








