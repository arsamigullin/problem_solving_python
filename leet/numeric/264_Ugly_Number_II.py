import collections
from heapq import heappop, heappush

# Approach is to precalculate the ugly numbers
class Ugly:
    # here we pre-calculate
    # all the ugly numbers
    # we start to compose these numbers starting from 1

    def __init__(self):
        heap = []
        heappush(heap, 1)
        seen = set()
        self.nums = [] # at the end it will have length 1690
        for i in range(1, 1691):
            cur_ugly = heappop(heap)
            self.nums.append(cur_ugly)
            for k in [2,3,5]:
                new_ugly = cur_ugly * k
                #we add to the heap only unseen values
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
        print(len(heap))

class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n):
        return self.ugly.nums[n-1]


# the same approach as above
class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]



class SolutionTLE:
    def nthUglyNumber(self, n: int) -> int:

        def is_ugly(n):

            if n == 1:
                return True
            while any(n % i == 0 for i in factors):
                for j in factors:
                    if n % j == 0:
                        n //= j
            return n == 1

        factors = {3, 2, 5}
        i = 1
        cnt = 0
        while cnt < n:
            if is_ugly(i):
                cnt += 1
            i += 1
        return i


class SolutionDP:
    def nthUglyNumber(self, n: int) -> int:
        dp = collections.defaultdict(bool)
        dp[0] = True
        num = 2
        while n>=2:
            val = num
            if val%2==0:
                val//=2
            elif val%3==0:
                val//=3
            elif val%5==0:
                val//=5
            if val!=num:
                if dp[val-1]:
                    dp[num-1] = True
                    num+=1
                    n-=1
                else:
                    num+=1
            else:
                num+=1
        return num-1

if __name__ == '__main__':
    s = SolutionDP()
    s.nthUglyNumber(456)
    s = Solution()
    s.nthUglyNumber(10)