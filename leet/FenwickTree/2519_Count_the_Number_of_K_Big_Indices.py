from typing import List


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s


class Solution1:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tree1 = BinaryIndexedTree(n)
        tree2 = BinaryIndexedTree(n)
        for v in nums:
            tree2.update(v, 1)
        ans = 0
        for v in nums:
            tree2.update(v, -1)
            # the reason we do v-1 is because i should be strictly less than idx, so we exclude v and do query for v-1
            ans += tree1.query(v - 1) >= k and tree2.query(v - 1) >= k
            tree1.update(v, 1)
        return ans


class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.LSOne(i) <= self.n:
                self.ft[i + self.LSOne(i)] += self.ft[i]

    def LSOne(self, n):
        return n & -n

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.LSOne(j)
        return s

    def update(self, i, val):

        while i <= self.n:
            self.ft[i] += val
            i += self.LSOne(i)


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = [0] * n
        ft1 = FTree([0] * n)
        for num in nums:
            ft1.update(num, 1)

        ft2 = FTree([0] * n)
        ans = 0
        for num in nums:
            ft1.update(num, -1)
            ans += ft1.query(1, num - 1) >= k and ft2.query(1, num - 1) >= k
            ft2.update(num, 1)
        return ans


class FTree:
    def __init__(self, arr):
        n = len(arr)
        self.ft = [0] * (n+1)
        for i in range(1, n+1):
            self.ft[i] = arr[i-1]
            if i + self.LsOne(i) <= n:
                self.ft[i + self.LsOne(i)] += self.ft[i]
        self.n = n


    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.LsOne(j)
        return s

    def update(self, i, delta):

        while i <= self.n:
            self.ft[i] += delta
            i += self.LsOne(i)





    def LsOne(self, i):
        return i & -i


if __name__ == '__main__':

    ft = FTree([1,1,1,1,1,1])
    ft.update()

    s = Solution()
    s.kBigIndices([2,3,6,5,2,3], 2)