import heapq
import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n ** 0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        # If n is a perfect square
        # we have to skip the duplicate
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1

        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1


class Solution:

    def heappush_k(self, heap, num, k):
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)

    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        nsqrt = int(math.sqrt(n))

        for i in range(1, nsqrt+1):
            if n%i == 0:
                self.heappush_k(heap, i, k)
                if n//i!=i:
                    self.heappush_k(heap, n//i, k)
        return -heapq.heappop(heap) if len(heap) == k else -1


if __name__ == '__main__':
    s = Solution()
    s.kthFactor(24, 5)
    s.kthFactor(36, 7)

    #[1,2,3,4,6,8,12,24]