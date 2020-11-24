from functools import reduce


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        tot = start
        s = start
        for i in range(1, n):
            s = start + 2 * i
            tot ^= s
        return tot


class Solution1:
    def xorOperation(self, n, start):
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        return (reduce(lambda x, y: x ^ y, nums))