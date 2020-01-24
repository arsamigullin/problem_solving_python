import itertools
import math
# my horrible solution
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        p = 1
        f = math.factorial(n - 1)
        while f * p < k:
            p += 1
        output = []
        nums = [str(j) for j in range(1, n + 1) if j != p]
        # backtrack()
        output = list(itertools.permutations(nums))
        return str(p) + ''.join(output[k - (f * (p - 1)) - 1])

# soluiton based on factorials
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return ''.join(output)


