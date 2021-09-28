import re
import operator
# similar 894
# 95. Unique Binary Search Trees II
# Divide and conquer
from typing import List


class Solution:
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        # let's consider an example 2*3-4*5
        # this composes array of operations
        # for our example we will have
        # [operator.mul, operator.sub, operator.mul]
        ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2]))



        # initially lo is 0 and hi is len of nums (which consists of only numbers, i.e. 2,3,4,5
        # since count of ops is equal len(nums) - 1 we can use lo ... hi to retrieve operations
        # for each recurse call we have divider i which splits nums[lo..hi] onto two parts
        # we handle nums[lo..i]  and nums[i+1..hi] by recursive calling and then join
        # each item from build(lo,i) and build(i+1,hi). We collect this result and return it
        # So, this result will be used in previous recursive call
        memo = {}
        def build(lo, hi):
            if f"{hi}|{lo}" in memo:
                return memo[f"{hi}|{lo}"]
            if lo == hi:
                return [nums[lo]]
            res = []
            for i in range(lo, hi):
                for a in build(lo, i):
                    for b in build(i + 1, hi):
                        print(f"{a} {b}")
                        res.append(ops[i](a, b))
            print(res)
            memo[f"{hi}|{lo}"] = res
            return res
            # return [ops[i](a, b)
            #         for i in range(lo, hi)
            #         for a in build(lo, i)
            #         for b in build(i + 1, hi)]

        print(build(0, len(nums) - 1))


class Solution2:

    def diffWaysToCompute(self, input, memo={}):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n


class Solution3:
    def diffWaysToCompute(self, s: str) -> List[int]:

        ops_map = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        ops = [] # for operations
        nums = [] # for numbers
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j].isnumeric():
                j += 1
            if i == j:
                ops.append(s[i])
                i += 1
            else:
                nums.append(int(s[i:j]))
                i = j

        memo = {}

        def helper(lo, hi):
            if lo == hi:
                return [nums[lo]]
            if (lo, hi) not in memo:
                res = []
                # IMPORTANT: i is the index for ops array
                # that is why it is withing [lo,hi-1] inclusive
                for i in range(lo, hi):
                    for left_res in helper(lo, i):
                        for right_res in helper(i + 1, hi):
                            res.append(ops_map[ops[i]](left_res, right_res))
                memo[(lo, hi)] = res
            return memo[(lo, hi)]

        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution3()
    s.diffWaysToCompute("2*3-4*5")
