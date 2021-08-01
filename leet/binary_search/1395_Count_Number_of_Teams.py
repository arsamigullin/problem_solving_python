
# brute force approach
from typing import List


class Solution4:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if (rating[i] > rating[j] > rating[k]) or (rating[i] < rating[j] < rating[k]):
                        count += 1
        return count


from bisect import bisect
from heapq import heapify
#
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def insert(x):
            i = bisect(tmp, x)
            tmp.insert(i, x)
            return i

        tmp = []
        l = list(map(insert, rating))
        print(l)
        tmp = []
        g = list(map(insert, rating[::-1]))
        g.reverse()
        print(g)
        counter = 0

        heap = [(v, i) for i,v in enumerate(rating)]
        heapify(heap)
        print(heap)


        length1 = len(rating)
        length2 = length1 - 1

        for i in range(length1):
            counter += l[i] * (length2 - i - g[i])
            counter += g[i] * (i - l[i])

        return counter
# this solution can be rewritten as Solution7 below
# Solution1 iliminates the need to call helper on reversed array
# thereby we reduce runtime
class Solution1:
    def numTeams(self, rating: List[int]) -> int:
        r, size = rating, len(rating)

        # compute statistics of sliding range
        left_smaller = [sum(r[i] < r[j] for i in range(0, j)) for j in range(size)]
        right_bigger = [sum(r[j] < r[k] for k in range(j + 1, size)) for j in range(size)]
        # ls = []
        # lr = []
        # for j in range(size):
        #     t = 0
        #     for i in range(0, j):
        #         t += (r[i] < r[j])
        #     ls.append(t)
        # for j in range(size):
        #     t = 0
        #     for k in range(j+1, size):
        #         t += (r[j] < r[k])
        #     lr.append(t)
        #
        # print(left_smaller, right_bigger, ls, lr)
        num_of_teams = 0
        # j slides from 0 to ( n-1 ), and j stands for the index of middle element
        for j in range(0, size):
            # this can be explained as follow
            # left_smaller stores count of (r[i] < r[j]), means at some index ind left_smaller stores count of the number that are bigger than rating[i]
            # right_bigger stores count of r[j] < r[k], means at some index ind right_bigger stores count of the number that are less than rating[k]
            # j is middle
            # to find how many commands in total of length 3 we need to just multiply
            num_of_ascending_team = left_smaller[j] * right_bigger[j]
            num_of_descending_team = (j - left_smaller[j]) * (size - 1 - j - right_bigger[j])
            num_of_teams += (num_of_ascending_team + num_of_descending_team)

        return num_of_teams


class Solution7:
    def numTeams(self, rating: List[int]) -> int:
        def helper(r):
            size = len(r)
            # compute statistics of sliding range
            left_smaller = [sum(r[i] < r[j] for i in range(0, j)) for j in range(size)]
            right_bigger = [sum(r[j] < r[k] for k in range(j + 1, size)) for j in range(size)]

            # j slides from 0 to ( n-1 ), and j stands for the index of middle element
            teams = 0
            for j in range(0, size):
                teams += left_smaller[j] * right_bigger[j]
            return teams

        return helper(rating) + helper(rating[::-1])


from heapq import heapify, heappop
from bisect import bisect, insort


class Solution2:

    def numTeams(self, rating: List[int]) -> int:
        triples = 0

        index_heap = [(rating[ri], ri) for ri in range(len(rating))]
        heapify(index_heap)
        index_list = list()
        t = heappop(index_heap)
        index_list.append(t[1])

        while index_heap:
            t = heappop(index_heap)
            b = bisect(index_list, t[1])

            lr = len(index_list) - b
            gr = (len(rating) - 1) - t[1] - lr
            ll = b
            gl = t[1] - ll

            triples += ((lr * gl) + (gr * ll))

            index_list.insert(b, t[1])

        return (triples)




# super sueper SLOW solution
class Solution3:
    def numTeams(self, rating: List[int]) -> int:
        count = 0

        def dfs(i, rat):
            nonlocal count
            if len(rat) == 3:
                if rat[0] > rat[1] > rat[2]:
                    count += 1
                return

            for j in range(i, len(rating)):
                rat.append(rating[j])
                dfs(j + 1, rat)
                rat.pop()

        dfs(0, [])
        rating = rating[::-1]
        dfs(0, [])
        return count

# The Product Rule: If there are n(A) ways to do A
# and n(B) ways to do B, then the number of ways to do
# A and B is n(A) × n(B). This is true if the number of
# ways of doing A and B are independent; the number of
# choices for doing B is the same regardless of which choice
# you made for A.

class Solution8:
    def numTeams(self, r: List[int]) -> int:

        # this function counts items that are less r[i]
        # if r is [1,2,1,5] and i is 3 (r[3]) the count is 3
        # so the num 5 has 3 (1,2,1) items to the left that are less than 5
        def count(r):
            n = len(r)
            asc = []
            for i in range(n):
                t = 0
                for j in range(i):
                    if r[i] > r[j]:
                        t+=1
                asc.append(t)

            desc = []
            for i in range(n):
                t = 0
                for j in range(i+1, n):
                    if r[j]>r[i]:
                        t+=1
                desc.append(t)

            return sum(a*b for a, b in zip(asc,desc))

        return count(r) + count(r[::-1])

# this is the optimized version of the Solution8
class Solution:
    def numTeams(self, A):
        L = len(A)
        result = 0
        for j in range(1,L-1):
            x, lo_L, lo_R, hi_L, hi_R = A[j], 0, 0, 0, 0
            for i in range(j):
                if A[i]<x:
                    lo_L += 1
                else:
                    hi_L += 1
            for k in range(j+1,L):
                if A[k]<x:
                    lo_R += 1
                else:
                    hi_R += 1
            result += lo_L*hi_R + hi_L*lo_R
        return result


# Version A:  [Top Speed] O(n log n) solution using SortedLists to calculate our 4 counting variables in Log(n) time.
from sortedcontainers import SortedList


class Solution:
    def count_low_high(self, sl, x):
        # this finds index to insert x
        # all items to the left are smaller than x
        lo = sl.bisect_left(x)
        # hence the items to the right are higher
        hi = len(sl) - lo
        return lo, hi

    def numTeams(self, A):
        result = 0
        left = SortedList()
        right = SortedList(A)
        for x in A:
            right.remove(x)
            lo_L, hi_L = self.count_low_high(left, x)
            lo_R, hi_R = self.count_low_high(right, x)
            result += lo_L * hi_R + hi_L * lo_R
            left.add(x)
        return result






if __name__ == '__main__':
    s = Solution8()
    s.numTeams([1,2,3,4])
    s = Solution1()
    s.numTeams([2,5,3,4,1])