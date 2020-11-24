from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        A = 0
        L = 0

        def helper(i, m, cur, turn=1):
            if i >= n:
                return 0
            res = 0
            for j in range(1, 2 * m + 1):
                if turn == 1:
                    res = max(helper(cur + piles[i:i+ j], max(m, j), turn ^ 1), 0)
                else:
                    res = max(helper(cur + piles[i:i+ j], max(m, j), turn ^ 1), 0)
            return res

        helper(0,1,0,1)
        print('done')

if __name__ == '__main__':
    s = Solution()
    s.stoneGameII([2,7,9,4,4])