class Solution(object):
    def pancakeSort(self, A):
        ans = []

        N = len(A)
        B = sorted(range(1, N + 1), key=lambda num: -A[num - 1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f + 1 - i
            ans.extend([i, N])
            N -= 1

        return ans


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i + 1, x])
            A = A[:i:-1] + A[:i]
        return res

if __name__ == '__main__':
    s = Solution()
    s.pancakeSort([3, 2, 4, 1])
