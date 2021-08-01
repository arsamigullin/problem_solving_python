from typing import List


class Solution:
    def makesquare(self, mst: List[int]) -> bool:
        mst.sort(reverse=True)
        perimeter = sum(mst)
        if perimeter % 4 != 0:
            return False
        sides = [0] * 4
        ps = perimeter // 4

        def helper(i):
            if i == len(mst):
                return sides[0] == sides[1] == sides[2] == sides[3]
            for j in range(4):
                sides[j] += mst[i]
                if sides[j] <= ps:
                    if helper(i + 1):
                        return True
                sides[j] -= mst[i]
            return False

        return helper(0)