import collections
import typing
List = typing.List
# since in the counter we store at most up to 3 elements
# we follow O(1) space complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                # find the difference between
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]

if __name__ == "__main__":
    s = Solution()
    s.majorityElement([1,2,3,4,1,2])