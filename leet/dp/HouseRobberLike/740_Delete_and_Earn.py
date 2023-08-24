import collections

# this problem is similar to house robber
# we have three variables to denote points
# pprev, prev, cur
# we cannot collect points from the nums that are equal value - 1 and value + 1, given value is current num
# therefore if the pr value equals value-1, we do pprev + cur, wehreas pres is always max(pprev, prev)
class Solution1(object):
    def deleteAndEarn(self, nums):
        points, pr, prev, pprev = collections.Counter(nums), None, 0, 0
        for value in sorted(points):
            # if we see that the neighbor num is value-1
            # that means we should not count points from value-1 (it is supposed to be removed from the list)
            # so the points equals value * count + pprev,
            # whereas for pprev is max of prev and pprev because on the next iteration it is not going to be the
            # points earned from the neighbor item
            # say we have array 2,3,5
            # on the first iteration it will go to else section and prev = 2
            # on the second iteration we have 3-1==2 and we go to if section
            if value-1 == pr:
                #                               # cur
                pprev, prev = max(pprev, prev), value * points[value] + pprev
            else:
                #                               # cur
                pprev, prev = max(pprev, prev), value * points[value] + max(pprev, prev)
            pr = value
        return max(pprev, prev)

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
    s = Solution1()
    s.deleteAndEarn([2, 2, 3, 3, 3, 4,4,4,6,6,6,6,6,6])
    s.deleteAndEarn([2,2,3,3,3,4])