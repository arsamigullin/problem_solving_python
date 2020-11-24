class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                # this is the formula of filling one cup
                # -1 means the current glass will take 1 cup
                # division 2 means it pours on both sides equally
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q
        # if we have poured being a large number
        # we will have A[query_row][query_glass] being a large number as well
        # but any excess should be poured out to the floor
        # and only 1 cup is left in the glass
        return min(1, A[query_row][query_glass])


if __name__ == '__main__':
    s = Solution()
    s.champagneTower(8,3,1)