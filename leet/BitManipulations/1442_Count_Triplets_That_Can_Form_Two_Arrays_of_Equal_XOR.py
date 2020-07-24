from typing import List


#O(n) O(n) space complexity
class Solution:
    def countTriplets(self, A):
        res = cur = 0
        count = {0: [1, 0]}
        for i, a in enumerate(A):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res


#O(n**2) O(1) space complexity
class Solution:
    def countTriplets(self, A):
        A.insert(0, 0)
        n = len(A)
        for i in range(n - 1):
            A[i + 1] ^= A[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if A[i] == A[j]:
                    res += j - i - 1
        return res

#O(n**2) O(1) space complexity
class Solution1:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)-1):
            xor = 0
            for j in range(i, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    res += j-i # len-1
        return res

if __name__ == '__main__':
    s = Solution()
    s.countTriplets([2,3,1,6,7])
    s.countTriplets([1,1,1,1,1])