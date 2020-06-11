from typing import List


class SolutionMy:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {}
        # link couples
        for i in range(1, len(row), 2):
            d[i - 1] = i
            d[i] = i - 1
        # print(d)
        count = 0
        i = 1
        while i < len(row) - 2:
            # if two person compose couple
            # move to the next two persons
            if row[i - 1] == d[row[i]]:
                i += 2
                continue
            else:
                j = i + 1
                # here we skip the couples where we no two persons are sitting next to each other
                # while j < len(row)-1 and row[i] != d[row[j+1]] and row[i-1] != d[row[j+1]] and row[i] != d[row[j]] and row[i-1] != d[row[j]]:
                while j < len(row) - 1 and not (
                        row[i] == d[row[j + 1]] or row[i - 1] == d[row[j + 1]] or row[i] == d[row[j]] or row[i - 1] ==
                        d[row[j]]):
                    j += 2
                    continue
                # for now we know for sure that either
                # i and j+1 compose couple or
                # i and j compose couple or
                # i-1 and j compose couple or
                # i-1 and j+1 compose couple or
                if row[i] == d[row[j + 1]]:
                    row[i - 1], row[j + 1] = row[j + 1], row[i - 1]
                elif row[i] == d[row[j]]:
                    row[i - 1], row[j] = row[j], row[i - 1]
                elif row[i - 1] == d[row[j]]:
                    row[i], row[j] = row[j], row[i]
                elif row[i - 1] == d[row[j + 1]]:
                    row[i], row[j + 1] = row[j + 1], row[i]
                count += 1
        return count



class SolutionXOR(object):
    def minSwapsCouples(self, row):
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1: continue
            ans += 1
            for j in range(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1], row[j] = row[j], row[i+1]
                    break
        return ans
if __name__ == '__main__':
    s = SolutionXOR()
    s.minSwapsCouples([3,2,0,5,4,1])
    s.minSwapsCouples([9,6,4,2,3,5,7,0,1])