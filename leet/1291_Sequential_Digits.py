from typing import List


class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        hi_len = len(str(high))
        for i in range(1, 10):
            num = 0
            for j in range(i, min(10, i + hi_len)):
                num = 10 * num + j
                if low <= num <= high:
                    res.append(num)

        # print(res)
        return sorted(res)

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        sample = '123456789'
        lo_len = len(str(low))
        hi_len = len(str(high))
        # for each length between low and high number
        for j in range(lo_len, hi_len + 1):
            # we extract number from sample
            for i in range(len(sample) + 1 - j):
                num = int(sample[i:i+j])
                # and check if it is in the range
                if low <= num <= high:
                    res.append(num)
        return res

if __name__ == '__main__':
    s = Solution()
    s.sequentialDigits(1000, 13000)