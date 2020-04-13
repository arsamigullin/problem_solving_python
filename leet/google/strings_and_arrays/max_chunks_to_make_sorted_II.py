import collections
# this problem
# https://leetcode.com/problems/max-chunks-to-make-sorted/

# similar problem
# https://leetcode.com/problems/max-chunks-to-make-sorted/
class SolutionCounted(object):
    '''
    this is solution is very similar to the one we got in
    max_chunks_to_make_sorted.py
    '''
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, (0,0)
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans
    # def maxChunksToSorted(self, arr):
    #     ans = ma = 0
    #     for i, x in enumerate(arr):
    #         ma = max(ma, x)
    #         if ma == i:
    #             ans += 1
    #     return ans


class SolutionShort(object):
    def maxChunksToSorted(self, arr):
        s1 = 0
        s2 = 0
        ans = 0
        for X, Y in zip(arr, sorted(arr)):
            s1 += X
            s2 += Y
            if s1 == s2:
                ans += 1
        return ans


class SolutionSlidingWindow(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr)):
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans

if __name__ == "__main__":
    s = SolutionCounted()
    s.maxChunksToSorted([2,1,3,4,4])
    s.maxChunksToSorted([1, 1, 0, 0, 1])
