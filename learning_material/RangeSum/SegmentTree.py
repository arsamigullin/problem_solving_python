from typing import List


class NumArray:
    tree = None
    n = None

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        if self.n:
            self.tree = [0] * 4 * len(nums)
            self.buildTree(nums, 0, 0, len(nums) - 1)

    '''
    arr: The original array
    index: the Segment tree index
    low: the lower bound
    high: the upper bound
    '''

    def buildTree(self, arr, index, low, high):
        if low == high:
            self.tree[index] = arr[low] if low < len(arr) else 0
        else:
            mid = (low + high) // 2
            self.buildTree(arr, 2 * index + 1, low, mid)
            self.buildTree(arr, 2 * index + 2, mid + 1, high)
            self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    '''
    i: the index that needs to be updated
    val: the value been updated
    index: the index of segment tree
    low: the lower bound
    high: the higher bound
    '''

    def update(self, i: int, val: int, index=0, low=0, high=float('inf')) -> None:
        if high == float('inf'):
            high = self.n - 1
        if low == high:
            self.tree[index] = val
        else:
            mid = (low + high) // 2
            if mid >= i:
                self.update(i, val, 2 * index + 1, low, mid)
            else:
                self.update(i, val, 2 * index + 2, mid + 1, high)
            self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    '''
    i: the lower bound of the query
    j: the upper bound of the query
    '''

    def sumRange(self, i: int, j: int, index=0, low=0, high=float('inf')) -> int:
        if high == float('inf'):
            high = self.n - 1
        if low > j or high < i:
            return 0
        if i <= low and j >= high:
            return self.tree[index]
        mid = (low + high) // 2
        if i > mid:
            return self.sumRange(i, j, 2 * index + 2, mid + 1, high)
        elif j <= mid:
            return self.sumRange(i, j, 2 * index + 1, low, mid)
        left = self.sumRange(i, mid, 2 * index + 1, low, mid)
        right = self.sumRange(mid + 1, j, 2 * index + 2, mid + 1, high)
        return left + right