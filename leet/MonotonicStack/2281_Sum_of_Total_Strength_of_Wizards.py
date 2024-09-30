from typing import List

from learning_material.PYTHON_LANG.itertools import accumulate


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(strength)

        right = [n] * n
        stack = []

        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right[stack.pop()] = i

            stack.append(i)

        print(right)

        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        print(left)

        # For the given index i, right array stores the index of the nearest item where strength[i] <= strength[right[i]]
        # For the given index i, left array stores the index of the nearest item where  strength[left[i]] < strength[i]
        # In other words, left and right provide start and end index of a subarray where strength[i] is the smallest item
        ppresum = list(accumulate(accumulate(strength, initial=0), initial=0))
        answer = 0

        # to understand why we need prefix sum of prefix sum, let's consider array [1 3 1 2] and suppose we are at index 2 (value1)
        # its left array is [-1, 0, -1, 2]
        # its right array is [2, 2, 4, 4]
        # based on left and right arrays we have left = -1 and right = 4
        # L = i - left = 2 - (-1) = 3
        # R = right - i = 4 - 2 = 2
        # it's prefix sum is
        # 0   1   4   5   7
        # a   b   c   d   e - for our convenience let's denote it using chars
        # based on original array [1 3 1 2] we have the following subarray index ranges
        # where value 1 under index 2 is the smallest numer
        # (0,2),(1,2),(2,2),(2,3),(1,3),(0,3)
        # their appropriate index ranges for prefix sum array
        # (0,3),(1,3),(2,3),(2,4),(1,4),(0,4), or with char representation it is
        # (d-a),(d-b),(d-c),(e-c),(e-b),(e-a)
        # 3d+3e-2a-2b-2c OR
        # 3(d+e) - 2(a+b+c)
        # to find d+e and a+b+c we need prefix sum of prefix sum

        for i in range(n):
            left_bound = left[i]
            right_bound = right[i]

            left_count = i - left_bound # number of items in the subarray to the left where strength[i] is the smallest item
            right_count = right_bound - i # number of items in the subarray to the right where strength[i] is the smallest item

            neg_presum = (ppresum[i + 1] - ppresum[i - left_count + 1]) % mod
            pos_presum = (ppresum[i + right_count + 1] - ppresum[i + 1]) % mod

            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            answer %= mod

        return answer


if __name__ == '__main__':
    s = Solution()
    s.totalStrength([1, 3, 1, 2])
