import re

import typing
List = typing.List

import re

# tons of redundant steps here
class SolutionMy:
    def findBlackPixel(self, picture: List[List[str]], N: int) -> int:
        rows = [''.join(arr[0]) for arr in zip(picture)]
        cols = [''.join(arr) for arr in zip(*picture)]
        tot = 0
        visited = set()
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and (i, j) not in visited:
                    n = list(re.finditer('B', rows[i]))
                    m = list(re.finditer('B', cols[j]))
                    pivotarr = rows[i]
                    cnt = 0
                    local_visited = set()
                    if len(m) == len(n) and len(m) == N:

                        for item in m:
                            s = item.start()
                            if rows[s] == pivotarr:
                                cnt += 1
                                local_visited.add((s, j))
                            else:
                                cnt = 0
                                local_visited = set()
                                break
                    visited.update(local_visited)
                    tot += cnt
        return tot


class SolutionShort:
    '''
        zip(*picture) is array of columns
        we start iterate over columns
        in each iteration we have a list with symbols of a particular column
        for example, the first iteration will have (W,W,W,W) but since it does not have B
        we will continue
        otherwise we count 'B' here and the TRICK is the index of 'B' represents index of row in picture this B at
        so, we have first row where first B resides, now we can count the first rows and compare with k


    '''
    def findBlackPixel(self, picture: List[List[str]], k: int) -> int:
        if not picture or not picture[0]: return 0

        count = 0
        for c in zip(*picture):
            if c.count('B') != k: continue
            first_row = picture[c.index('B')]
            if first_row.count('B') != k: continue
            if picture.count(first_row) != k: continue
            count += 1
        return count * k

if __name__ == "__main__":
    s= SolutionShort()
    s.findBlackPixel([["W","B","W","B","B","W"],
                      ["W","B","W","B","B","W"],
                      ["W","B","W","B","B","W"],
                      ["W","W","B","W","B","W"]],
3)
