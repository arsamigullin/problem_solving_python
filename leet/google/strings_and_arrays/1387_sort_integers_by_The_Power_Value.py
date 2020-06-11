class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = {}

        def ordfunc(x):
            if x in d:
                return d[x]
            if x == 1:
                return 0
            d[x] = (ordfunc(x // 2) if x % 2 == 0 else ordfunc(x * 3 + 1)) + 1
            return d[x]

        nums = list(range(lo, hi + 1))
        nums.sort(key=ordfunc)
        # print(nums)
        return nums[k - 1]