from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        # it is quite natural to sort the array
        # each array element will be considered as a root
        # since the array is sorted we think of the left side elements
        # to be the children
        arr.sort()
        # store indexes
        index = {v: i for i, v in enumerate(arr)}
        MOD = 10 ** 9 + 7
        dp = [1] * len(arr)
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0: # arr[j] is left child
                    right = v // arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    s.numFactoredBinaryTrees([2, 4, 8])
