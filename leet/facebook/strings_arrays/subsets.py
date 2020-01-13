# this is back tracking algo
# 1. we go to the end, form set
# 2. return it and add to the list with current item (!IMPORTANT)
# 3. then the returned set we merging with current item
# 4. at the end do not forget to append []
class MySolution:
    def subsets(self, nums: list) -> list:

        def find(nums, i):
            if i >= len(nums):
                return []
            arr = find(nums, i + 1)
            res = [[nums[i]]] + arr
            for a in arr:
                r = [nums[i]] + a
                res.append(r)
            return res

        res = find(nums, 0)
        res.append([])
        return res

# short and good solution
class Solution:
    def subsets(self, nums):
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets

# itertools
def subsets(self, nums):
    return [s for n in range(len(nums)+1)
            for s in itertools.combinations(nums, n)]

#
def subsets(self, nums):
    return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
            for mask in range(2 ** len(nums))]