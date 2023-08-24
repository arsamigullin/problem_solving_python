from typing import List

#O(n**2)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        up = [0] * n
        down = [0] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)

        return 1 + max(down[-1], up[-1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 2:
            return n
        up = [0] * n
        down = [0] * n
        up[0] = down[0] = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] - nums[j] > 0:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] - nums[j] < 0:
                    down[i] = max(down[i], up[j] + 1)
                else:
                    up[i] = up[i - 1]
                    down[i] = down[i - 1]

        return max(up[-1], down[-1])

# O(n) O(n)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        up = [0] * n
        down = [0] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return 1 + max(down[-1], up[-1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        up = 1
        down = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(down, up)


if __name__ == '__main__':
    s = Solution()
    s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])