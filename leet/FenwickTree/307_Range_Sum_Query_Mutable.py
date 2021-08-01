from typing import List


class NumArray:
    '''
    a = [1,2,3,4,5,6]
    fenwick tree as follow
    ft = [0,1,3,3,10,5,11]
    every index stores cumulative sum in the range [i-lsone(i)+1, i-lsone(i)+2, ... i]
    index 2 (ft[2]=3) in ft responsible for the range [1..2]
    index 3 (ft[2]=3) is responsible for the range [3..3]
    index 4 (ft[2]=10) is responsible for the range [1..4]
    index 5 (ft[2]=5) is responsible for the range [5..5]
    index 6 (ft[2]=11) is responsible for the range [5..6]
    '''
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)
        self.f = f
        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def sumRange(self, i, j):
        return self.helper(i + 1, j + 1)

    def helper(self, i, j):
        if i > 1:
            return self.helper(1, j) - self.helper(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)

        return s

    def update(self, i, v):
        dif = -(self.f[i] - v)
        self.f[i] = v
        i += 1
        while i <= self.n:
            self.ft[i] += dif
            i += self.lsone(i)

    def select(self, k):
        p = 1
        while (p * 2) <= self.n: p *= 2

        i = 0
        while p > 0:
            if k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p
            p //= 2

        return i + 1

def lsone(i):
    return i&(-i)


class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.sums += (val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sums - sum(self.nums[:left]) - sum(self.nums[right + 1:])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == '__main__':
    s = NumArray([1,2,3,4,5])
    s.select(15)
    print(s.ft)
    s = NumArray([1, 2,3,4,5,6])
    s.update(0, 3)
    s = NumArray([9,-8])
    s.update(0,3)
    print(s.sumRange(1,1))
    s.sumRange(0,1)

    for i in range(10):
        k = 1
        while True:
            j = i - lsone(i) + k
            k+=1
            print(i, j)
            if j>=i:
                break



