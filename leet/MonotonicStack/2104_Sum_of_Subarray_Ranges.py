from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # nums = [1,7,8,9,5]
        n = len(nums)
        stack = []
        answer = 0
        for right in range(n + 1):
            # say we have right = 4 (i.e. nums[right] is 5)
            # nums = [1,7,8,9] and nums[right] is 5
            # stack contains only increasing items
            # 1st iteration
            # 9 >= 5, indices: left=2 mid=3 right=4
            # nums[mid] is 9, so by mid-left and right-mid we count how many subarrays have 9 as a minimum number (actually 1)
            # 2nd iteration
            # 8>=5, indices: left=1 mid=2 right=4
            # nums[mid] is 8, so by mid-left and right-mid we count how many subarrays have 8 as a minimum number (actually 2, [8] and [8,9])
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        stack = []
        # stack = [6,5,4] right is 9
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        return answer

if __name__ == '__main__':
    s = Solution()
    s.subArrayRanges([1, 7, 8, 9, 10])
    s.subArrayRanges([1,7,8,9,4])