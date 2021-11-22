class FenwickTree:
    def __init__(self, n):
        self.n = n + 1
        self.ft = [0] * (self.n)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)
        return s

    def update(self, i, val):
        while i < self.n:
            self.ft[i] += val
            i += self.lsone(i)

    def lsone(self, i):
        return i & -i


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BIT O(nlogn)
        # this part is easy
        # we just merging the initial array and doubled array
        # sort them and removing duplicates
        new_nums = nums + [x * 2 for x in nums]
        sorted_set = sorted(list(set(new_nums)))
        tree = FenwickTree(len(sorted_set))
        res = 0
        ranks = {}
        # here we are assigning indexes to uniq values
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1
        #FAQ
        # Q: why removing duplicates works?
        # A: because duplicate numbers will still be counted
        # for example [3,2,2,1] and doubled one [6,4,4,2], after merging [1,2,3,4,6]
        # when iterating over nums, we have two 2's there. Every 2 will be referring to the same index, hence we
        # will count 2*nums[j] for every 2

        #Q: why we call query with ranks[n]-1.
        #A: ranks stores 1-based indexes but we do not want to count the number itself because the condition is strict
        # nums[i]>2*nums[j]

        #Q: why do we need to reverse nums
        #A: this is because of problem condition
        # "A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j]"
        # reversing array we count and store pairs for the jth elements
        # later on, the ith elements uses that result

        for n in nums[::-1]:
            res += tree.query(1, ranks[n] - 1)
            tree.update(ranks[n * 2], 1)

        return res

if __name__ == '__main__':
    s = Solution()
    s.reversePairs([5,4,3,2,1])