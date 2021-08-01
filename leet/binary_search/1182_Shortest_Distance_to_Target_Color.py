import bisect
import collections
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for i, c in enumerate(colors):
            d[c].append(i)
        res = []
        for t, c in queries:
            if c not in d:
                res.append(-1)
                continue
            l = bisect.bisect_left(d[c], t)
            if l == len(d[c]):
                l-=1
            if l-1 >=0 and d[c][l] > t:
                res.append(min(abs(d[c][l]-t),abs(d[c][l-1]-t)))
            elif l+1<len(d[c]) and d[c][l] < t:
                res.append(min(abs(d[c][l]-t),abs(d[c][l+1]-t)))
            else:
                res.append(abs(d[c][l]-t))
        return res

# shorter
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list)
        for i,c in enumerate(colors):
            hashmap[c].append(i)

        query_results = []
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                query_results.append(-1)
                continue

            index_list = hashmap[color]
            # use bisect from Python standard library
            # more details: https://docs.python.org/3/library/bisect.html
            insert = bisect.bisect_left(index_list, target)

            # compare the index on the left and right of insert
            # make sure it will not fall out of the index_list
            left_nearest = abs(index_list[max(insert - 1, 0)] - target)
            right_nearest = abs(index_list[min(insert, len(index_list) - 1)] - target)
            query_results.append(min(left_nearest, right_nearest))

        return query_results


class SolutionPrecompute:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # initializations
        n = len(colors)
        rightmost = [0, 0, 0]
        leftmost = [n - 1, n - 1, n - 1]

        distance = [[-1] * n for _ in range(3)]

        # looking forward
        for i in range(n):
            color = colors[i] - 1
            for j in range(rightmost[color], i + 1):
                distance[color][j] = i - j
            rightmost[color] = i + 1

        # looking backward
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(leftmost[color], i - 1, -1):
                # if the we did not find a target color on its right
                # or we find out that a target color on its left is
                # closer to the one on its right
                if distance[color][j] == -1 or distance[color][j] > j - i:
                    distance[color][j] = j - i
            leftmost[color] = i - 1

        return [distance[color - 1][index] for index,color in queries]

if __name__ == '__main__':
    s = SolutionPrecompute()
    s.shortestDistanceColor([1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]])