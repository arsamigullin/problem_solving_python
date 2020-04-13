import collections
import bisect
from typing import List

#     300. longest-increasing-subsequence
#     334. increasing-triplet-subsequence
#     354. russian-doll-envelopes
#     646. maximum-length-of-pair-chain
#     673. number-of-longest-increasing-subsequence
#     674. longest-continuous-increasing-subsequence
#     1395. count-number-of-teams


class MySolution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # we maintainin this dp where each element consists of
        # max sequence length at i element (cur_max_len) and sequence count of that length at i element
        dp = [(1,1)] * len(nums)
        max_len = 1
        max_count = 1

        for i in range(1, len(nums)):
            for j in range(i):
                # once the current item is greater than previous
                if nums[i] > nums[j]:
                    cur_max_len, cur_count = dp[i]
                    prev_max_len, prev_count = dp[j]
                    # see if current length at i is equal the length of previous element + 1
                    if prev_max_len + 1 == cur_max_len:
                        cur_count+=prev_count
                    # but if previous length is greater than length at i element
                    elif prev_max_len + 1 > cur_max_len:
                        # we reset count and max_len
                        cur_max_len = prev_max_len + 1
                        cur_count=prev_count
                    dp[i] = (cur_max_len, cur_count)

            # here before leaving we check each element visited and
            # updating the global variables
            cur_max_len, cur_count = dp[i]
            if max_len == cur_max_len:
                max_count += cur_count
            elif cur_max_len> max_len:
                max_count = cur_count
                max_len = cur_max_len
        return max_count


class Solution:
    """
    https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/199093/short-python-50ms-beats-100-with-binary-search

    300. longest-increasing-subsequence
    334. increasing-triplet-subsequence
    354. russian-doll-envelopes
    646. maximum-length-of-pair-chain
    673. number-of-longest-increasing-subsequence
    674. longest-continuous-increasing-subsequence
    1395. count-number-of-teams
    """

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0

        cnter = collections.defaultdict(collections.Counter)
        cnter[-1][float("-inf")] = 1

        lis = []
        for num in nums:
            idx = bisect.bisect_left(lis, num)
            if idx == len(lis):
                lis += [num]
            else:
                lis[idx] = num
            cnter[idx][num] += sum(cnter[idx - 1][pre] for pre in cnter[idx - 1] if pre < num)
        return sum(cnter[len(lis) - 1].values())

if __name__ == '__main__':
    s = Solution()
    s.findNumberOfLIS([1,3,5,4,7])
    s.findNumberOfLIS([1,1,2,2,2,2,3,5,5,5])
    s.findNumberOfLIS([1,2,3,5,5,5])
    s.findNumberOfLIS([2,2,2,2,2])