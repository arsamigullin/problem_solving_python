from typing import List

# related
# 523
# 209
# 713

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        _sum = 0
        max_len = 0
        for i, n in enumerate(nums):
            _sum += 1 if n == 1 else -1
            if _sum in d:
                max_len = max(max_len, i-d[_sum])
            else:
                d[_sum] = i
        return max_len

if __name__ == "__main__":
    s = Solution()
    s.findMaxLength([0,1,0,1])