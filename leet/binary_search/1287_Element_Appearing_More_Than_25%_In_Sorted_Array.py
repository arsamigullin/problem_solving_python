class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        def bisec_right(arr, target):
            lo = 0
            hi = len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if target < arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        def bisect_left(arr, target):
            lo = 0
            hi = len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        n = len(arr)
        for i in [n // 4, n // 2, (n * 3) // 4]:
            left_index = bisect_left(arr, arr[i])
            right_index = bisect_right(arr, arr[i])
            if right_index - left_index > n // 4:
                return arr[i]
        return -1
