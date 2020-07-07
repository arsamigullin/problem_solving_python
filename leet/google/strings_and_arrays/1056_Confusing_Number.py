import collections


class Solution:
    def confusingNumber(self, N: int) -> bool:
        nums = list(str(N))
        d = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
        rotated = collections.deque()
        for n in nums:
            if n not in d:
                return False
            rotated.appendleft(d[n])
        return ''.join(rotated) != ''.join(nums)

