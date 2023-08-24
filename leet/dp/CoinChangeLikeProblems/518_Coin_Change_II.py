import collections
from typing import List


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        cnt_dict = collections.defaultdict(int)

        def helper(a, i):
            if a == 0:
                return 1
            if i == n:
                return 0
            if (a, i) not in memo:
                if coins[i] > a:
                    memo[(a, i)] = helper(a, i + 1)
                else:
                    memo[(a, i)] = helper(a - coins[i], i) + helper(a, i + 1)

                #print(f"amount {a}, i {i}, num of ways {memo[(a, i)]}")
            cnt_dict[(a,i)]+=1
            return memo[(a, i)]

        helper(amount, 0)
        print(cnt_dict)

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
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0] * (amount + 1)
        dp[0] = 1
        '''
        Think of this implementation in layers term
        Each layer is associated with a specific coin
        we have dp array and we are going to put layer by layer to that
        the first layer starts with coin = 1, we get dp = [1,1,1,1,1,1]
        the second layer start with coin = 2, we get dp = [1,1,2,2,3,3]
        the third layer starts with coin = 5, we get dp = [1,1,2,2,3,4]
        Note: the next layer uses the result of previous layer
        '''
        for c in coins:
            for a in range(c, amount + 1):
                if a >= c:
                    dp[a] += dp[a - c]

        return dp[-1]  # helper(amount, 0)

if __name__ == '__main__':
    s = Solution()
    s.change(5, [1, 2, 5])
    # s.change(6,[2,2,1])