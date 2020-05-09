import collections
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = set()
        for a,b in points:
            d.add((a,b))
        #print(d)
        _m = float('inf')
        count = 0
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(1, len(points)):
                count+=1
                x2, y2 = points[j]
                difx = abs(x1-x2)
                dify = abs(y1-y2)
                if difx == 0 or dify==0:
                    continue
                if (x1,y2) in d and (x2,y1) in d:
                    _m = min(_m, difx*dify)
        print(count)
        return 0 if _m == float('inf') else _m

class Solution1:
    def minAreaRect(self, points: List[List[int]]) -> int:
        d = set()
        for a,b in points:
            d.add((a,b))
        count = 0
        _m = float('inf')
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i, len(points)):
                count += 1
                x2, y2 = points[j]
                difx = abs(x1-x2)
                dify = abs(y1-y2)
                if difx == 0 or dify==0:
                    continue
                if (x1,y2) in d and (x2,y1) in d:
                    _m = min(_m, difx*dify)
        print(count)
        return 0 if _m == float('inf') else _m

class Solution2(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        # let's compose the dictionary
        # where key is x coordinate
        for x, y in points:
            columns[x].append(y)
        # this links coordinate x and two coordinates y
        # if we have vertical line on the graph it always has common x for two y coordinates
        lastx = {}
        ans = float('inf')

        # we do sort columns because lastx[y1, y2] = x is supposed to store the latest x
        # let suppose we have these coordinates
        # if we will not sort x coordinates
        # there possible situation where lastx[y1, y2] = x will be overwritten by not smallest value
        # for exmaple we have this order [x3,x1,x2], when we are at x2 the lastx[y1, y2] contains x1
        # the area between x1 and x2 is  less than between x1 and x3 but in this situation
        # we did not count area between x2 and x3
        '''
        y    ________
        |   |      | |
        |   |______|_|
        |   x1    x2 x3
        |
        |___________________ x
        '''
        for x in sorted(columns):
            column = columns[x]
            #column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, abs(x - lastx[y1,y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

if __name__ == '__main__':
    s2 = Solution2()
    s2.minAreaRect([[1,2],[3,2],[1,3],[5,5],[2,0],[4,5],[3,4],[1,4],[1,5],[0,0],[0,5],[0,4],[4,2],[3,5],[5,2],[2,4],[4,0]])
    s2.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]])
    s = Solution()
    s.minAreaRect([
        [1,1],[1,3],[3,1],[3,3],[4,1],[4,3], [1,1],[1,3],[3,1],[3,3],[4,1],[4,3],[1,1],[1,3],[3,1],[3,3],[4,1],[4,3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],[1,1],[1,3],[3,1],[3,3],[4,1],[4,3], [1,1],[1,3],[3,1],[3,3],[4,1],[4,3],[1,1],[1,3],[3,1],[3,3],[4,1],[4,3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],
    ])
    s = Solution1()
    s.minAreaRect([
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3],
        [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],
        [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3], [1, 1], [1, 3],
        [3, 1], [3, 3], [4, 1], [4, 3],
    ])