import time



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

class SolutionBacktrack:
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

import math
class SolutionKnuth:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def helper(arr):
            i = len(arr) - 2
            # from the end find the first arr[i] that is
            # less than arr[i+1]
            while i >= 0 and arr[i] > arr[i + 1]:
                i -= 1

            # if i is lesss than zero
            # this means nubers in reversed order, just reverse them
            if i < 0:
                arr.reverse()
                return

            # starting from the end find first arr[j] that is greater than arr[i]
            j = len(arr) - 1
            while i < j and arr[i] >= arr[j]:
                j -= 1

            # swap numbers under i and j
            arr[i], arr[j] = arr[j], arr[i]
            # reverse numbers between i+1 and end of arr
            arr[i + 1:] = arr[i + 1:][::-1]

        output = []
        # the total permutation count is
        n = math.factorial(len(nums))

        for _ in range(n):
            helper(nums)
            output.append(nums[:])
        return output


if __name__ == "__main__":
    s = SolutionBacktrack()
    start = time.time()
    s.permute([1,2,3,4,5,6,7,8,9,10,11])
    end = time.time()
    print(end - start)
    s= SolutionKnuth()
    start = time.time()
    s.permute([1,2,3,4,5,6,7,8,9,10,11])
    end = time.time()
    print(end-start)