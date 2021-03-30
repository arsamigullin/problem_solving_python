import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counts = [0] * 101
        for n in arr:
            counts[n] += 1

        res = 0
        for i in range(100):
            if counts[i] == 0:
                continue
            j, k = i, 100
            while j <= k:
                if j + k > target - i:
                    k -= 1
                elif j + k < target - i:
                    j += 1
                else:
                    if i == j == k:
                        # this formula for combinations
                        # C(n,r) = n!/(r!(n-r)!)
                        # where counts[i] * (counts[i] - 1) * (counts[i] - 2) is P(n,r) because
                        # P(n,3) = n!/(n-r)! = n * (n-1) * (n-2)
                        # so, to obtain Combinations we need P(n,3)/r!
                        res += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
                    elif i == j:
                        # the same is here
                        # since i == j we want to find a combinations of length 2
                        # P(n,2) = count[i] * (count[i]-1)
                        # but to find combinations we also need
                        # P(n,2)/2!
                        res += counts[i] * (counts[i] - 1) * counts[k] // 2 # that is why we have two  here
                    elif j == k:
                        # the same as above
                        res += counts[i] * counts[j] * (counts[j] - 1) // 2
                    else:
                        # if all numbers are different, then we just multiply all of them
                        res += counts[i] * counts[j] * counts[k]
                    j += 1
                    k -= 1
        return res % (10 ** 9 + 7)


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = collections.Counter(arr)

        res = 0
        if target % 3 == 0:
            n = c.get(target // 3, 0)
            res += n * (n - 1) * (n - 2) // 6

        keys = sorted(c.keys())
        for k in keys:
            n = c[k]
            if n > 1 and k < target and target - 2 * k != k:
                res += c.get(target - 2 * k, 0) * n * (n - 1) // 2

        for i in range(len(keys)):
            if keys[i] >= target // 3: break
            for j in range(i + 1, len(keys)):
                new = target - (keys[i] + keys[j])
                if new <= keys[j]: break
                if new in c:
                    res += c[keys[i]] * c[keys[j]] * c[new]

        return res % (10 ** 9 + 7)


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        A.sort()
        MOD = 10 ** 9 + 7
        ans = 0

        for i, x in enumerate(A):
            T = target - A[i]
            j, k = i + 1, len(A) - 1

            while j < k:
                if A[j] + A[k] > T:
                    k -= 1
                elif A[j] + A[k] < T:
                    j += 1
                # A[j]+A[k] = T but the numbers are not equal to each other
                elif A[j] != A[k]:
                    left = right = 1
                    while j < k - 1 and A[j] == A[j + 1]:
                        left += 1
                        j += 1
                    while k > j + 1 and A[k] == A[k - 1]:
                        right += 1
                        k -= 1

                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    # because the items between j and k are equal in this case
                    # because of that we also want to break
                    num = k - j
                    ans += num * (num + 1) // 2
                    ans %= MOD
                    break
        return ans

