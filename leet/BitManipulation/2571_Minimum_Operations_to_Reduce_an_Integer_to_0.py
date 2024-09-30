class Solution:
    def minOperations(self, n: int) -> int:
        res = 0
        while n > 0:
            print(bin(n))
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2
        return res

if __name__ == '__main__':
    s = Solution()
    s.minOperations(39)
    s.minOperations(int('11101',2))
    s.minOperations(8)
    s.minOperations(2)
