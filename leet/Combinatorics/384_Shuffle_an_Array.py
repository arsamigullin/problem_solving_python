import random
from typing import List

# Knuth permutation algorithm
class Solution:

    def __init__(self, nums: List[int]):
        self.orig = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        i = len(self.nums) - 2
        while i >= 0 and self.nums[i] > self.nums[i + 1]:
            i -= 1

        if i < 0:
            self.nums.reverse()
            return self.nums

        j = len(self.nums) - 1

        while j > i and self.nums[i] > self.nums[j]:
            j -= 1

        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        lo, hi = i + 1, len(self.nums) - 1
        while lo < hi:
            self.nums[lo], self.nums[hi] = self.nums[hi], self.nums[lo]
            lo += 1
            hi -= 1

        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

# Fisher-Yates Algorithm

#https://blog.codinghorror.com/the-danger-of-naivete/
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array