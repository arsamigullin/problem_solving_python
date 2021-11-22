import bisect


class Solution:
    def countRangeSum(self, nums, lower, upper):

        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)

        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)
            #print(BITree)

        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            # sum_j is a just some cumulative sum
            # let's say sum_j is 11
            # lower = 2
            # upper = 8
            # doing sum_j - lower = 11 - 2 = 9 and sum_j - upper = 11-8 = 3
            # we actually got two cumsum 9 and 3. We now search for 3 and 9 in the sorted prefix array sortSum and getting their index
            # BIT stores count for every cumsum, so we pass the- indices of 3 and 9 to the BIT
            # to count how many cumsum in the BIT in the range between 3 and 9
            # NOTE: even if 3 and 9 is out of range 2 and 8, it will not count 9, because
            # update(bisect.bisect_left(sortSum, sum_j) + 1) counts only cumsum that exists in prefix
            f = bisect.bisect_right(sortSum, sum_j - lower)
            s = bisect.bisect_left(sortSum, sum_j - upper)
            sum_i_count = count(f) - count(s)
            #print(sum_i_count, s, f)
            res += sum_i_count
            ind = bisect.bisect_left(sortSum, sum_j) + 1
            print(sum_i_count, ind, s, f)
            update(ind)
        return res




class FenwickTree:
    def __init__(self, n):
        self.ft = [0] * (n + 1)
        self.n = n

    def lsone(self, i):
        return i & -i

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, val):

        while i <= self.n:
            self.ft[i] += 1
            i += self.lsone(i)


class Solution2:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        '''
        a = [1,2,3,4,5,6]
        fenwick tree as follow
        ft = [0,1,3,3,10,5,11]
        every index stores cumulative sum in the range [i-lsone(i)+1, i-lsone(i)+2, ... i]
        index 2 (ft[2]=3) in ft responsible for the range [1..2]
        index 3 (ft[3]=3) is responsible for the range [3..3]
        index 4 (ft[4]=10) is responsible for the range [1..4]
        index 5 (ft[5]=5) is responsible for the range [5..5]
        index 6 (ft[6]=11) is responsible for the range [5..6]

        a = [3,5,7]
        prefSums = [0,3,8,15]
        ft = [0,0,0,0,0]
        '''

        n = len(nums)
        prefSums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefSums[i] = prefSums[i - 1] + nums[i - 1]
        sortedPrefSums = sorted(prefSums)
        ft = FenwickTree(len(sortedPrefSums))
        count = 0
        for i, pref in enumerate(prefSums):
            f = bisect.bisect_right(sortedPrefSums, pref - lower)
            s = bisect.bisect_left(sortedPrefSums, pref - upper)
            count += ft.query(s + 1, f)
            bl = bisect.bisect_left(sortedPrefSums, pref)
            ft.update(bl + 1, 1)
        return count

if __name__ == '__main__':
    s = Solution2()
    s.countRangeSum([3,5,7], 1, 12)
    #s.countRangeSum([-2,5,-1], -2, 2)