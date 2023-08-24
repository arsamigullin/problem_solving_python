# this problem is very similar to coin change problem
# in coin change problem we have coins and target
# in the loop from 1 to target we find the minimum coins requires to get target
# if coin is less or equal than current target we do find minimum

# the count of combinations of target equals
# dp[target] = dp[target - num[i]]
class Solution:
    def combinationSum4(self, nums: list, target: int) -> int:
        d = [0] * (target + 1)
        d[0] = 1
        # for each number till target
        for m in range(1, target + 1):
            # we go over the given numbers from which the target should be gotten
            for n in nums:
                if n <= m:
                    d[m] += d[m - n]
        return d[-1]


# note though, this task is very similar to 377. Combination Sum IV
# but there are a huge difference between them - order of loops
# here loop with coins comes first
# the reason is that in this problems we are looking for number of combinations. To get combinations
# we visit every coin only once. I.e. we pick up the coin and then looking to see how every coin contributes to the
# number of combinations for each amount from 1 to Amount. We do layering where each layers is associated with coin.
# We have as many layers as coins
# The opposite in Conbination Sum IV problem. Number of layers are not equal to number of coins because
# we iterate over coins for every amount from 1 to Amount.
# !! if coins are sorted !!
# the dp will be populating from the beginning toward end because amount will be increasing
# with every iteration over Amount
# in Conbination Sum IV problem we are looking for number of permutations
# say [1,2,5] and Amount is 5
# Let's assume the current amount is 3. For that amount we iterate over all the coins, i.e. different permutations
# of amount 3 that starts with 1 and then with 2 (since 5 is > 3, it is skipped)
# this does not happen in Coin Change 2 problem

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        memo = {}

        def helper(remain):
            if remain == 0:
                return 1
            if remain not in memo:
                res = 0
                for n in nums:
                    if n <= remain:
                        res += helper(remain - n)
                memo[remain] = res
            return memo[remain]

        return helper(target)


if __name__ == "__main__":
    s = Solution()
    s.combinationSum4([1, 2, 5], 5)
    s.combinationSum4([1,2,3],4)