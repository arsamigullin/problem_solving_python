from typing import List


class FenwickTree:
    def __init__(self, size):
        print(size)
        self.size = size + 1
        self.ft = [0] * self.size

    def lsone(self, i):
        return i & (-i)

    def update(self, i, val):
        i += 1
        while i < self.size:
            self.ft[i] += val
            i += self.lsone(i)

    def query(self, i):
        res = 0
        while i >= 1:
            res += self.ft[i]
            i -= self.lsone(i)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ft = FenwickTree(2 * (10 ** 4) + 1)
        offset = 10 ** 4 # this is to cover negative numbers
        result = []
        for num in reversed(nums):
            '''
            [5,2,6,4,1]
            note: every num in the array is an index in the Fenwick Tree
            we start in reversed order
            1. call ft.query(num+offset), this returns sum of all items in the range [0..(nums+offset)]
            2. update current num (which is index in the Fenwick tree) with 1, in other words, increase count of the 
            number num
            
            important to understand, calling ft.query on the current (num+offset) will bring the sum of all items in
            the range [0..(nums+offset)] 
            '''
            smaller_count = ft.query(num + offset)
            result.append(smaller_count)
            ft.update(num + offset, 1)
        return reversed(result)

if __name__ == '__main__':
    s= Solution()
    s.countSmaller([5,2,6,4,1])