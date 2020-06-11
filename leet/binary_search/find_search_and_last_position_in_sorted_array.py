# the idea is we keep searching until start == end
# to find left most we introduced left parameter. If it is True we keep the hi at mid. That way we find leftmost index
# When finding rightmost the left is False. And in case of matching we just increasing leftside boundary (mid + 1)
# Need to remember
# after the leftmost found, we need to confirm it is equal the target
# after the rightmost is found substract 1 at the end
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]


if __name__ == "__main__":
    s = Solution()
    s.searchRange([5, 7, 7, 8, 8, 10], 6)


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = end - (end - start) // 2
            if nums[mid] == target:
                j = i = mid
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i + 1, j - 1]
            elif nums[mid] > target:
                end = end - 1
            else:
                start = mid + 1
        return [-1, -1]
