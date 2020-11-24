import collections
import math
from typing import List
import itertools


class Solution1:
    def generatePalindromes(self, s: str) -> List[str]:
        c = collections.Counter(s)
        cnt = 0
        odd_char = ''
        for k, v in c.items():
            if v % 2 == 1:
                cnt += 1
                odd_char = k
        if cnt > 1:
            return []
        elif cnt == 1:
            c[odd_char] -= 1

        string = []
        for k, v in c.items():
            l = [k] * (v // 2)
            string.extend(l)

        def permute(arr):

            i = len(arr) - 2

            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1

            if i < 0:
                arr.reverse()
                return

            j = len(arr) - 1

            while i < j and arr[j] < arr[i]:
                j -= 1

            arr[i], arr[j] = arr[j], arr[i]

            lo = i + 1
            hi = len(arr) - 1

            while lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1

        # n = math.factorial(len(string))
        # res = set()
        # for _ in range(n):
        #     permute(string)
        #     res.add(''.join(string) + odd_char + ''.join(string[:][::-1]))

        print(list(itertools.permutations(string)))

        #return res


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        c = collections.Counter(s)
        cnt = 0
        odd_char = ''

        for k, v in c.items():
            if v % 2 == 1:
                cnt += 1
                odd_char = k
        if cnt > 1:
            return []
        elif cnt == 1:
            c[odd_char] -= 1

        string = []
        for k, v in c.items():
            l = [k] * (v // 2)
            string.extend(l)
        res = set()

        def permute(st, l, ch):
            if l == len(st):
                res.add(''.join(string) + ch + ''.join(string[:][::-1]))
            else:
                for i in range(l, len(st)):
                    # at the very first iteration l==i will always True
                    # that will allow us to add to the res the initial string as it is
                    if st[l] != s[i] or l == i:
                        st[l], st[i] = st[i], s[l]
                        permute(st, l + 1, ch)
                        st[l], st[i] = st[i], s[l]

        permute(string, 0, odd_char)
        return res


if __name__ == '__main__':
    s = Solution()
    s.generatePalindromes("aabb")