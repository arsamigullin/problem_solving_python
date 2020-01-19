import random

# the very fast and simple solution
# Algo
# 1. Collect indices for all the matches with target
# 2. random.choice(ind)
class Solution:

    def __init__(self, nums: list):
        self.nums = nums

    def pick(self, target: int) -> int:
        # import random
        ind = []
        for i, n in enumerate(self.nums):
            if n == target:
                ind.append(i)
        return random.choice(ind)




class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans, cnt = 0, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, cnt) == 0:
                    ans = i
                cnt += 1
        return ans

if __name__ == "__main__":
    s = Solution([1,2,3,3,3])
    s.pick(3)
    s.pick(3)
    s.pick(3)
    s.pick(3)