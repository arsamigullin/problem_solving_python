from typing import List

# this problem
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# 1130. Minimum Cost Tree From Leaf Values

#270 ms
class Solution:
    '''
    This approach uses DP. We are given the list of leaf values. We need to find sum of all non leaf nodes
    tree with given leaves.
    we do split array where i is a cut point

    :param arr:
    :return:
    '''
    def mctFromLeafValues(self, arr: List[int]) -> int:
        d = {}

        def helper(start, end):
            key = f"{start}|{end}"
            if key in d:
                return d[key]
            if end - start == 1:
                d[key] = (0, arr[start])
                return d[key]
            if end - start == 2:
                d[key] = (arr[start] * arr[end - 1], max(arr[start], arr[end - 1]))
                return d[key]
            min_sum = float('inf')
            cur_max_val = float('-inf')
            for i in range(start + 1, end):
                cur_sum1, max_val1 = helper(start, i)
                cur_sum2, max_val2 = helper(i, end)
                # this is how we find min_sum for current node
                min_sum = min(min_sum, (max_val1 * max_val2) + cur_sum1 + cur_sum2)
                cur_max_val = max(max_val1, max_val2)
            d[key] = (min_sum, cur_max_val)
            return d[key]

        return helper(0, len(arr))[0]

#800 ms
# this is the same as above.
# 1. The difference is it composes key from all the items in array passed
# 2. It uses arr[:]
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        d = {}
        def helper(items):
            # it
            key = '|'.join(map(str, items))
            if key in d:
                return d[key]
            if len(items) == 1:
                d[key] = (0, items[0])
                return d[key]
            if len(items) == 2:
                d[key] = (items[0] * items[1], max(items[0], items[1]))
                return d[key]

            min_sum = float('inf')
            for i in range(1, len(items)):
                cur_sum1, max_val1 = helper(items[:i])
                cur_sum2, max_val2 = helper(items[i:])
                min_sum = min(min_sum, (max_val1 * max_val2) + cur_sum1 + cur_sum2)
            d[key] = (min_sum, max(items))
            return d[key]

        res = helper(arr)[0]
        return res

# one of the fast solutions
class Solution:

    '''
    the trick of this solution is we find the smallest sum without examining extra cases
    1. in loop we find index of the smallest element
    2. then we product value under i and value of the smallest neighbor. So we have the smallest value of non-leaf node
    3. we add it to the cost

    '''
    def mctFromLeafValues(self, arr: List[int]) -> int:
        cost = 0
        # 6 2 4
        # 1 iteration
        #  i is 1 (2 is min)
        # arr[i-1:i] is 6 and arr[i+1:i+2] is 4.  min is 4. 4*2 = 8
        # cost is 8
        # 2 iteration
        # i is 1. (4 is min)


        while len(arr) > 1:
            i = arr.index(min(arr))
            cost += min(arr[i-1:i]+arr[i+1:i+2])*arr.pop(i)
        return cost


import math


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if arr is None or len(arr) < 2:
            return 0
        if len(arr) == 2:
            return arr[0] * arr[1]

        sortedArr = [n for n in arr]
        sortedArr.sort()

        output = 0

        while len(arr) > 1:
            # find the smallest
            smallest = sortedArr.pop(0)

            # pair it with its smallest neighbor
            smallestIndex = arr.index(smallest)
            l = math.inf
            if smallestIndex != 0:
                l = arr[smallestIndex - 1]
            r = math.inf
            if smallestIndex + 1 < len(arr):
                r = arr[smallestIndex + 1]
            output += min(l, r) * smallest
            arr.pop(smallestIndex)

        return output