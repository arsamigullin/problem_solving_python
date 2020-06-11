from typing import List
from typing import List

# prefix sum
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        # before we calculate prefix sum
        def getpref(m, lim):
            d = {}
            i = len(A) - m
            j = len(A)
            tot = d[i] = sum(A[i:j])
            while i >= lim:
                i -= 1
                tot += A[i]
                tot -= A[j - 1]
                j -= 1
                d[i] = max(tot, d[i + 1])
            return d

        # this will use prefix sum
        def find(L, M, d):
            sum_nums = sum(A[:L])
            i, j = 0, L
            total = sum_nums + d[j]
            while j < len(A) - M:
                sum_nums -= A[i]
                sum_nums += A[j]
                i += 1
                j += 1
                total = max(total, sum_nums + d[j])
            return total

        return find(L, M, getpref(M, L)) if L == M else max(find(L, M, getpref(M, L)), find(M, L, getpref(L, M)))


class Solution3:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:

        def find(m, n):
            nums_sum = sum(A[:m])
            i, j = 0, m
            total = nums_sum + sum(A[m:n + m] or [0])
            while j < len(A) - n + 1:
                k, p = j, j + n
                s = sum(A[k:p])
                total = max(total, s + nums_sum)
                while p < len(A):
                    s -= A[k]
                    s += A[p]
                    total = max(total, s + nums_sum)
                    k += 1
                    p += 1

                nums_sum -= A[i]
                nums_sum += A[j]
                i += 1
                j += 1

            return total

        return max(find(L, M), find(M, L))



if __name__ == '__main__':
    s = Solution()
    s.maxSumTwoNoOverlap([1, 0, 1], 1, 1)
    s.maxSumTwoNoOverlap([8, 20, 6, 2, 20, 17, 6, 3, 20, 8, 12], 5, 4)
    s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2)
    s.maxSumTwoNoOverlap([4, 0, 1], 2, 1)
    s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3)
