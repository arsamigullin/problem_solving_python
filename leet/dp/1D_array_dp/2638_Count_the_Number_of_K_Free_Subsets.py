# similar to
# 2597. The Number of Beautiful Subsets
import collections
from bisect import bisect
from collections import defaultdict
from functools import reduce
from operator import mul
from typing import List


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        def getCount(vs):
            vs.sort()
            sol1 = sol2 = 1
            prev = -k
            for v in vs:
                if prev + k == v:
                    sol = sol2 + sol1
                else:
                    sol = sol1 * 2
                sol1, sol2 = sol, sol1
                prev = v
            return sol1
        table = defaultdict(list)
        for num in nums:
            table[num % k].append(num)
        tot = 1
        for vs in table.values():
            tot *= getCount(vs)
        return tot


class Solution1:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        modToSubset = collections.defaultdict(set)

        for num in nums:
            modToSubset[num % k].add(num)

        prevNum = -k
        skip = 0
        pick = 0

        for subset in modToSubset.values():
          for num in sorted(subset):
            skip, pick = skip + pick, 1 + skip + (0 if num - prevNum == k else pick)
            prevNum = num

        return 1 + skip + pick

class Solution:
    def countTheNumOfKFreeSubsets(self, A, k):
        count = [collections.Counter() for i in range(k)]
        for a in A:
            count[a % k][a] += 1
        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for a in sorted(count[i]):
                v = pow(2, count[i][a])
                if prev + k == a:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)
                prev = a
            res *= dp0 + dp1
        return res


'''
I.e. we do not include into subset adjacent number
say we have this input [-2,2,3,5,8] with k=5
when calling dp func 
with a=8 it will do dfs and call dp func 
with a=3, which will call dp func 
with a=-2

call with a=-2 returns (1,1)
call with a=3 returns (2,1)


All numbers in the array are unique
if we have numbers where the next number is on k greater thant prev one, i.e.
-2,3,8,11
then the number of subsets with no two items with difference k are 
{}, -2, 3, 8, 11, -2 8, -2 11, 3 11 
there are 8 of them. This fits into fibonacci sequence
index 0 1 2 3 4 5
fib   1 2 3 5 8 13

In essence, here nuber of subsets are actually number of combinations, i.e. 2^n
So, if we have array with no two elements with difference k, the the number of 
combinations (aka number of subsets) is 2^4=16

So, we want to group all items where the next item is on K greater than prev item.
This is why there is a condition in the loop if not count[a + k]. We want to start with the largest item and 
inside of loop we do dp(a-k) visiting the previous item which is smaller on k
By doing that we know for sure that fibonacci numbers will work for that 
for the a-k not in count, it will always return 1,1
return dp0 + dp1, dp0 * (pow(2, count[a]) - 1)

dp0,dp1 = 1,0
1+0,1*(2^1-1) = 1, 1*(2-1) = 1,1

As we already know all the number in the array are unique, therefore in the dp function we can just return
dp + dp1, dp0
If numbers in the array are not unique, we return
dp0 + dp1, dp0 * (pow(2, count[a]) - 1)
'''
class Solution5:
    def countTheNumOfKFreeSubsets(self, A, k):
        count = collections.Counter(A)

        def dp(a):
            dp0, dp1 = dp(a - k) if a - k in count else (1, 0)
            return dp0 + dp1, dp0 # * (pow(2, count[a]) - 1)

        return reduce(mul, (sum(dp(a)) for a in count if not count[a + k]))

if __name__ == '__main__':
    s = Solution5()
    res = s.countTheNumOfKFreeSubsets([-2,2,3,5,8], 5)
    #print(res)
    #s.countTheNumOfKFreeSubsets([10,5,9,11], 20)
    #s.countTheNumOfKFreeSubsets([2,3,5,8,9,13], 5)