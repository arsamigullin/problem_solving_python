class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        i, j = 0, 1

        def binary_search(target, isLower):
            res = -1
            start = 0
            end = len(nums) - 1
            if isLower:
                if target > nums[end]:
                    return -2
            else:
                if target < nums[start]:
                    return -2

            while start <= end:
                mid = start + (end - start) // 2
                if isLower:
                    if nums[mid] <= target:
                        res = mid
                        start = mid + 1
                    else:
                        end = mid - 1
                else:
                    if nums[mid] >= target:
                        res = mid
                        end = mid - 1
                    else:
                        start = mid + 1
            return res

        start = binary_search(lower, True)
        if start == -2:
            return []
        elif start == -1:
            start = 0
        end = binary_search(upper, False)
        if end == -2:
            return []
        elif end == -1:
            end = nums[-1]
        i, j = start, start + 1
        res = []
        while j < len(nums[start:end]):
            left = nums[i] + 1
            right = nums[j] - 1
            if left == right:
                res.append(str(nums[left]))
            elif left < right:
                res.append(f"{nums[left]->nums[right]}")
            i += 1
            j += 1

        return res