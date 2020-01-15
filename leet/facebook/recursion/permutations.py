class MySolution:
    def permute(self, nums: list):
        res = []
        def find(s, permutation):
            if len(s) == 0:
                res.append(list(permutation))
                return
            for item in s:
                permutation.append(item)
                find(s.difference({item}), permutation)
                permutation.pop()

        find(set(nums), [])
        return res

class ShortSolution:
    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]



class ShortSolutionDecompose:
    def permute(self, nums):
        res = []
        for i, n in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i+1:]):
                res.append([n] + p)
            return res



import  itertools
class IterToolSolution:
    def permute(self, nums):
        return list(itertools.permutations(nums))

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # return this back
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == "__main__":
    s= Solution()
    s.permute([1,2,3])