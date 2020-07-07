from typing import List


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = {()}
        nums.sort()
        for n in nums:
            for sub in subsets.copy():
                subsets.add((n,) + sub)
        return subsets


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.findSubsets(nums, 0, [], res)
        return res

    def findSubsets(self, arr, index, r, res):
        res.append(r[:])
        for i in range(index, len(arr)):
            if i == index or arr[i] != arr[i - 1]:
                r.append(arr[i])
                self.findSubsets(arr, i + 1, r, res)
                r.pop()


if __name__ == '__main__':
    s = Solution2()
    s.subsetsWithDup([1, 2, 2, 3])
