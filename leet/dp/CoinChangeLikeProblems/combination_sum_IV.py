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
            for j in range(len(nums)):
                if nums[j] <= m:
                    d[m] += d[m - nums[j]]
        return d[-1]


if __name__ == "__main__":
    s = Solution()
    s.combinationSum4([1,2,3],4)