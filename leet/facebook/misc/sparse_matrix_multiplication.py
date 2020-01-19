# Note
# any([0,0,0,0]) is False
# any([0,0,0,1]) is True
# to multiply two matrices take this into account:
# the columns count of the first matrix must be equal the rows of the second matrix
# the result matrix will consist of rowF and columnS
# Where rowF is the count of rows of the first matrix and columnS is the count of columns of the second matrix
# suppose we have 2 dimensional array
B = [[7, 2, 3],[4, 5, 6],[0, 0, 1]]
# to get row and an array at this row we do
enumerate(B)
# note : this we return tuple (index, ([array],)
enumerate(zip(B))
# to get col and an array at this col we do
enumerate(zip(*B))



# the brute force approach
class SolutionBruteForce:
    def multiply(self, A: list, B: list) -> list:
        result = [[0]*len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for b in range(len(B[0])): # this is columns
                s = 0
                for j in range(len(A[0])):
                    s += A[i][j] * B[j][b] # in A we move through row, on B we move through column
                result[i][b] = s
        print(result)


# this algo is pretty much the same
# the only difference is the approach of finding a product
class SolutionSimple:
    def multiply(self, A: list, B: list) -> list:
        if not A or not A[0] or not B or not B[0] or len(A[0]) != len(B):
            return []

        n1, n2, n3 = len(A), len(B), len(B[0])
        res = [[0 for _ in range(n3)] for i in range(n1)]
        for rowA in range(len(A)): # rows of A
            for colA in range(len(A[0])): # columns of A
                if A[rowA][colA] != 0:
                    for colB in range(len(B[0])): # columns of B
                        rowB = colA
                        res[rowA][colB] += A[rowA][colA] * B[rowB][colB]
        print(res)
        return res



class Solution:
    def multiply(self, A: list, B: list) -> list:
        result = [[0] * len(B[0]) for _ in range(len(A))]
        for i, row in enumerate(A):
            if any(row):
                for j, col in enumerate(zip(*B)):
                    if any(col):
                        result[i][j] = sum(x * y for x, y in zip(row, col))
        return result
if __name__ == "__main__":
    A = [
        [1, 0, 0],
        [-1, 0, 3]
    ]

    B = [[7, 0, 0],[0, 0, 0],[0, 0, 1]]
    A = [[1,2,3],[4,5,6]]
    B = [[1,3], [2,5],[4,2]]
    s = SolutionSimple()
    s.multiply(A, B)
    s = Solution()
    s.multiply(A,B)