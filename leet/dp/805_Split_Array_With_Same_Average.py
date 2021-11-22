from typing import List
'''
The solution for this problem is built based on the fact that
if the array of size n can be splitted into group A and B with same mean, assuming A is the smaller group, then
(could not find the source of this statement, it is on leetcode https://leetcode.com/problems/split-array-with-same-average/discuss/120667/C%2B%2B-Solution-with-explanation-early-termination-(Updated-for-new-test-case) )
totalSum/n = Asum/k = Bsum/(n-k), where k = A.size() and 1 <= k <= n/2;
Asum = totalSum*k/n, which is an integer. So we have totalSum*k%n == 0;

NOTE: Asum is essentially integer. Because Asum is just sum of some integers in nums
which also means that (totalSum*k)%n == 0

'''

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        tot = sum(nums)

        # given sum_so_far
        # we need to determine if some integers in nums exist such that subtracting them from sum_so_far
        # leads to 0
        # and if at some point sum_so_far == 0 with its length == 0(arr_len) that means we could find
        # these numbers from nums
        # from that totalSum/n = Asum/k = Bsum/(n-k) means that the second array with sum Bsum also exist
        def helper(sum_so_far, arr_len, i):
            if arr_len == 0:
                return sum_so_far == 0
            if sum_so_far < 0 or arr_len < 0:
                return False
            if i >= n:
                return False
            if (sum_so_far, arr_len, i) not in memo:
                memo[(sum_so_far, arr_len, i)] = helper(sum_so_far - nums[i], arr_len - 1, i + 1) or helper(sum_so_far, arr_len,
                                                                                                            i + 1)
            return memo[(sum_so_far, arr_len, i)]
        # here i is the possible length of subarray with total sum (i * tot) // n
        return any(helper((i * tot) // n, i, 0) for i in range(1, 1 + n // 2) if (i * tot) % n == 0)

# Brute force
class Solution2:
    def splitArraySameAverage(self, nums: List[int]) -> bool:

        n = len(nums)

        def helper(i, sumA, sumB, a, b):
            if i >= n:
                return a != 0 and b != 0 and sumA / a == sumB / b
            if not helper(i + 1, sumA + nums[i], sumB, a + 1, b):
                return helper(i + 1, sumA, sumB + nums[i], a, b + 1)
            else:
                return True

        return helper(0, 0, 0, 0, 0)

if __name__ == '__main__':
    s = Solution2()
    print(s.splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))