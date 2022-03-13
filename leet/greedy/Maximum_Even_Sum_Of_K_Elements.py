# microsoft
# We are given a list (sticking with the Python tongue cause I cannot stop loving it!)
# of positive integers and we have to find the maximum even sum for K elements from the list. If we can’t find one, we return -1.

# source
# https://levelup.gitconnected.com/maximum-even-sum-of-k-elements-ca060ab3a9fd

import time
import heapq
class Solution:
    def find(self, A, K):
        even = []
        odd = []
        for a in A:
            if a % 2 == 1:
                odd.append(a)
            else:
                even.append(a)
        odd.sort(reverse=True)
        even.sort(reverse=True)
        e_length = len(even)
        o_length = len(odd)
        if e_length == 0:
            return -1
        if e_length + o_length < K:
            return -1
        ei = 0
        oi = 0
        res = 0
        while K > 0:
            if K % 2 == 1:
                res += even[ei]
                K -= 1
                ei += 1
                continue
            elif ei + 1 < e_length and oi + 1 < o_length:
                res += max(even[ei] + even[ei + 1], odd[oi] + odd[oi + 1])
                ei += 2
                oi += 2
            elif ei + 1 < e_length:
                res += even[ei] + even[ei + 1]
                ei += 2
            elif oi + 1 < o_length:
                res += odd[oi] + odd[oi + 1]
                oi += 2
            # this is question to ask interviewer
            else:
                return -1
            # else:
            #     return -1
            K -= 2
        return res

    def solve2(self, A, K):
        if not A or K == 0:
            return -1

        def add_item(arr, size, item):
            if len(arr) < size:
                heapq.heappush(arr, item)
                to_add = item
            else:
                evicted = heapq.heappushpop(arr, item)
                to_add = item - evicted
            return to_add
        odd_size = K - (K%2==1)
        even_size = K
        single_even = 0
        even = []
        odd = []
        sum_even = 0
        sum_odd = 0
        for a in A:
            if a%2 == 0:
                sum_even+=add_item(even, even_size, a)
                single_even = max(single_even, a)
            elif a%2==1:
                sum_odd+=add_item(odd, odd_size, a)
        tot = -1
        if len(even) == even_size:
            tot = max(tot, sum_even)
        if len(odd) == odd_size and len(even)>0:
            tot = max(tot, sum_odd + single_even if K%2== 1 else 0)
        return tot




import random
if __name__ == '__main__':
    s = Solution()

    large = [random.randint(0,50) for _ in range(10**7)]
    K = 10**6
    start_time = time.time()
    print(s.find([-1, -2, -2], 3))

    print(s.find([4, 2, 6, 7, 8], 3))
    print(s.find([1, 1, 1], 3))
    print(s.find([1, 1], 3))
    print(s.find([1], 3))
    print(s.find([1], 3))
    print(s.find([], 0))
    print(s.find([1, 2], 1))
    print(s.find([1, 2], 2))
    print(s.find([2, 4, 10, 3, 5], 3))
    print(s.find([5, 5, 1, 1, 3], 3))
    print(s.find([4, 2, 6, 7, 8], 3))
    print(s.find([5, 5, 2, 4, 3], 3))
    print(s.find([-1, -2, -2], 3))
    print(s.find([1, 2, 4, 11], 100))
    print(s.find([1, 2, 4, 11], 1))
    print(s.find([5, 5, 1, 1, 3], 3))
    print(s.find(large, K))
    print(time.time()-start_time)

    start_time = time.time()
    print("Hello world")
    print(s.solve2([-1, -2, -2], 3))
    print(s.solve2([4, 2, 6, 7, 8], 3))
    print(s.solve2([1, 1, 1], 3))
    print(s.solve2([1, 1], 3))
    print(s.solve2([1], 3))
    print(s.solve2([1], 3))
    print(s.solve2([], 0))
    print(s.solve2([1, 2], 1))
    print(s.solve2([1, 2], 2))
    print(s.solve2([2, 4, 10, 3, 5], 3))
    print(s.solve2([5, 5, 1, 1, 3], 3))
    print(s.solve2([4, 2, 6, 7, 8], 3))
    print(s.solve2([5, 5, 2, 4, 3], 3))
    print(s.solve2([-1, -2, -2], 3))
    print(s.solve2([1, 2, 4, 11], 100))
    print(s.solve2([1, 2, 4, 11], 1))
    print(s.solve2([5, 5, 1, 1, 3], 3))
    print(s.solve2(large, K))
    print(time.time() - start_time)
