from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []

        def helper(n):
            if n == 0:
                result.append(0)
                return

            helper(n - 1)
            current_size = len(result)
            mask = 1 << (n - 1)
            for i in range(current_size - 1, -1, -1):
                result.append(result[i] | mask)

        helper(n)
        return result

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        seq_len = 1<<n
        for i in range(seq_len):
            num = i^i>>1
            result.append(num)
        return result

if __name__ == '__main__':
    s = Solution()
    s.grayCode(4)