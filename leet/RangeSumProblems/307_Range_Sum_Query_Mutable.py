from typing import List


class NumArray1:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        self.buildTree(self.tree, nums)

    def buildTree(self, tree, nums):
        i, j = self.n, 0
        # filling leaves
        # leaves take n nodes
        # n - 1 nodes of the tree are composed by merging childrens starting from leaves
        while i < 2 * self.n:
            tree[i] = nums[j]
            i += 1
            j += 1
        # this is merge process
        # filling other nodes of the tree
        for i in range(self.n - 1, 0, -1):
            tree[i] = tree[i * 2] + tree[i * 2 + 1]

    def update(self, pos: int, val: int) -> None:
        pos += self.n
        self.tree[pos] = val
        while pos > 0:
            lo = pos
            hi = pos
            if pos % 2 == 0:
                hi = pos + 1
            else:
                lo = pos - 1
            self.tree[pos // 2] = self.tree[lo] + self.tree[hi]
            pos //= 2

    def sumRange(self, l: int, r: int) -> int:
        l += self.n
        r += self.n
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]
                l += 1
            if r % 2 == 0:
                s += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)




# fenwick tree approach
class NumArray2:

    def __init__(self, nums: List[int]):
        # init the fenwick tree
        self.nums = nums
        self.bit = [0] + nums
        self.n = len(self.nums)
        for i, num in enumerate(nums):
            p = i + (i & -i)
            if p < len(self.bit):
                self.bit[p] += self.bit[i]

    def update(self, i: int, val: int) -> None:
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1  # bit starts from 1
        while i < len(self.bit):
            self.bit[i] += diff
            i += (i & -i)

    def get_sum(self, i: int) -> int:
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= (i & -i)
        return result

    def sumRange(self, i: int, j: int) -> int:
        return self.get_sum(j + 1) - self.get_sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


# SQRT decomposition

#TO DO

if __name__ == '__main__':
    s = NumArray1([1, 3, 5])
    s.sumRange(1,2)
    s.update(1, 6)
    s.sumRange(1,2)