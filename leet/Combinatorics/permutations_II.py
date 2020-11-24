from typing import List


class Solution:
    def permuteUnique(self, nums: list):
        res = []
        def find(s, permutation):
            if len(s) == 0:
                res.append(list(permutation))
                return
            visited = set()
            for i, item in enumerate(s):
                if item in visited:
                    continue
                visited.add(item)
                permutation.append(item)
                find(s[:i]+s[i+1:], permutation)
                permutation.pop()

        find(nums, [])
        return res

class SolutionShort:
    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]
        return perms


class Solution4:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def helper(j, comb):
            if len(comb) >= n:
                res.append(comb[:])
                return
            visited = set()
            for i in range(j, n):
                if nums[i] not in visited:
                    comb.append(nums[i])
                    helper(i + 1, comb)
                    comb.pop()
                    visited.add(nums[i])

        helper(0, [])
        return res


if __name__ == "__main__":
    s = Solution4()
    s.permuteUnique([1,2,3])