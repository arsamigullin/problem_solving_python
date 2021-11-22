import collections


class Solution(object):
    def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)

if __name__ == '__main__':
    s = Solution()
    s.deleteAndEarn([2,2,3,3,3,4])