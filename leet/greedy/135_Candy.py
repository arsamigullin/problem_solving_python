from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        # collect rating from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # collect rating from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        '''
        ratings = [4,3,1,2], then
        left = [1,1,1,2]
        right = [3,2,1,1]
        '''

        res = 0
        for l, r in zip(left, right):
            res += max(l, r)
        return res