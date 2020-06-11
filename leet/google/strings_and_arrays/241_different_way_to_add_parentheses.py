import re
import operator
# similar 894
# Divide and conquer
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


if __name__ == "__main__":
    s = Solution2()
    s.diffWaysToCompute("2*3-4*5")
