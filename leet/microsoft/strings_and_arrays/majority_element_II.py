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


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        val1 = None
        count2 = 0
        val2 = None

        for n in nums:
            if val1 == n:
                count1 += 1
            elif val2 == n:
                count2 += 1
            elif count1 == 0:
                val1 = n
                count1 += 1
            elif count2 == 0:
                val2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        if nums.count(val1) > len(nums) // 3:
            res.append(val1)
        if nums.count(val2) > len(nums) // 3:
            res.append(val2)

        return res



if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1,2,3,4,1,2,1,1]))