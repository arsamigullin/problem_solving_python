import collections
from typing import List

# this is preferable way to solve permutation with duplicates problem
class Solution:
    def permuteUnique(self, nums: list):
        res = []
        c = collections.Counter(nums)
        n = len(nums)

        def find(perms):
            if len(perms) == n:
                res.append(perms[:])
                return
            for ch in c:
                if c[ch] > 0:
                    c[ch] -= 1
                    perms.append(ch)
                    find(perms)
                    perms.pop()
                    c[ch] += 1

        find([])
        return res


class Solution3:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], collections.Counter(nums))

        return results

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
    s = Solution3()
    s.permuteUnique([1,1,2])
    s.permuteUnique([1,2,2,3])