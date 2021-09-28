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

# clean code java version
#https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/757373/C%2B%2B-Segment-Tree-Solution-w-explanation-Accepted

class STree:
    def __init__(self, l):
        self.l = l
        self.n = len(l)
        self.st = [0] * (4 * self.n)
        self.islazy = [False] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def left(self, p):
        return p << 1

    def right(self, p):
        return (p << 1) + 1

    def build(self, p, l, r):
        if (l == r):
            self.st[p] = l
        else:
            self.build(self.left(p), l, (l + r) // 2)
            self.build(self.right(p), (l + r) // 2 + 1, r)
            p1 = self.st[self.left(p)]
            p2 = self.st[self.right(p)]
            if self.l[p1] <= self.l[p2]:
                self.st[p] = p1
            else:
                self.st[p] = p2

    def _q(self, p, pl, pr, fr, to):
        if fr > pr or to < pl:
            return -1, -1
        if self.islazy[p]:
            return fr, self.lazy[p]
        if fr <= pl and to >= pr:
            return self.st[p], self.l[self.st[p]]

        res1 = self._q(self.left(p), pl, (pl + pr) // 2, fr, to)
        res2 = self._q(self.right(p), (pl + pr) // 2 + 1, pr, fr, to)

        if (res1[0] == -1):
            return res2
        elif res2[0] == -1:
            return res1
        elif res1[1] <= res2[1]:
            return res1
        else:
            return res2

    def _u(self, p, pl, pr, fr, to, newval):
        if fr > pr or to < pl:
            return self.st[p]

        if fr == pl and to == pr:
            if fr == to:
                self.l[pl] = newval
                self.islazy[p] = False
            else:
                self.lazy[p] = newval
                self.islazy[p] = True

            self.st[p] = fr
            return self.st[p]

        pm = (pl + pr) // 2

        if self.islazy[p]:
            self.islazy[p] = False
            self.islazy[self.left(p)] = True
            self.islazy[self.right(p)] = True
            self.lazy[self.left(p)] = self.lazy[p]
            self.lazy[self.right(p)] = self.lazy[p]
            self.st[self.left(p)] = pl
            self.st[self.right(p)] = pm

        p1 = self._u(self.left(p), pl, pm, max(fr, pl), min(to, pm), newval)
        p2 = self._u(self.right(p), pm + 1, pr, max(fr, pm + 1), min(to, pr), newval)

        if self.l[p1] <= self.l[p2]:
            self.st[p] = p1
        else:
            self.st[p] = p2
        return self.st[p]

    def q(self, fr, to):
        return self._q(1, 0, self.n - 1, fr, to)[0]

    def u(self, fr, to, val):
        return self._u(1, 0, self.n - 1, fr, to, val)


class SegmentTree:
    def __init__(self, a):
        self.n = len(a)
        self.t = [0] * (4*self.n)
        self.a = a

    def build(self, v, tl, tr):
        if tr==tl:
            self.t[v] = tl
            return
        self.build(2*v,tl,(tl+tr)//2)
        self.build(2*v+1,(tl+tr)//2 + 1, tr)
        self.t[v] = self.t[2*v+1] if self.a[self.t[2*v]]>self.a[self.t[2*v+1]] else self.t[2*v]

    def query(self, v, tl, tr, l, r):
        if l<r:
            return -1
        if tr==r and tl==l:
            return self.t[v]
        m = (tr+tl)//2
        i = self.query(2*v,tl,m,l,min(m,r))
        j = self.query(2*v+1,m+1,tr,max(l,m+1),r)
        if i == -1 or j ==-1:
            return j*i*-1
        return  j if self.a[i]>self.a[j] else i

    def rec(self, od, l, r):
        if l>r:
            return 0
        m = self.query(1,0, self.n-1,l,r)
        return self.a[m]-od+self.rec(self.a[m],l,m-1) + self.rec(self.a[m],m+1,r)

if __name__ == '__main__':
    l = [18, 17, 13, 19, 15, 11, 20]
    st = STree(l)
    print(st.q(0,10))