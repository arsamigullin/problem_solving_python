class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        rows = set()
        cols = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0


class Solution2:
    def setZeroes(self, M):
        m, n = len(M[0]), len(M)
        # if the top row has any 0
        r1 = any(M[0][j] == 0 for j in range(m))
        # if the leftmost column has any 0
        c1 = any(M[i][0] == 0 for i in range(n))

        #
        for i in range(1, n):
            for j in range(1, m):
                if M[i][j] == 0: M[i][0] = M[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if M[i][0] * M[0][j] == 0: M[i][j] = 0

        if r1:
            for i in range(m): M[0][i] = 0

        if c1:
            for j in range(n): M[j][0] = 0

if __name__ == '__main__':
    s = Solution2()
    s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
    s.setZeroes([[1,2,3,4],[5,0,5,2],[8,9,2,0],[5,7,2,1]])