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

        # to understand why we need prefix sum of prefix sum
        # 0   1   2   3   4   5   6   7   8
        #                     ai
        #     L-----------------
        #                     -------------R
        # L-i+1(a)                        R+i-1(h)
        #    L-i+2(b)                R+i-2(g)
        #         L-i+3(c)        R+i-3(f)
        #              L-i+4(d)
        #                     (e)
        # L is 5 and R is 4
        # item under index 5 is the smallest item to the subarray enclosed between L and R
        # however, the subarray between L and R includes many subarray
        # let's suppose that we composed regular prefix sum array and each of the letters a,b,c,d,e,f,g,h denote
        # value under appropriate index in that prefix sum array
        # In this case, we can calculate the following total sum of all the subarrays enclosed between L and R
        # (e-a)+(e-b)+(e-c)+(e-d)+
        # (f-a)+(f-b)+(f-c)+(f-d)+(f-e)
        # (g-a)+(g-b)+(g-c)+(g-d)+(g-e)
        # (h-a)+(h-b)+(h-c)+(h-d)+(h-e) =>
        # (e+e+e+e)-(a+b+c+d)+
        # (f+f+f+f+f)-(a+b+c+d+e)
        # (g+g+g+g+g)-(a+b+c+d+e)
        # (h+h+h+h+h)-(a+b+c+d+e) =>
        # 5f + 5g + 5h + 4e - 4a - 4b - 4c - 4d - 3e
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
