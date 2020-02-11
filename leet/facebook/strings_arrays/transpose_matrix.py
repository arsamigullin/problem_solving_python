import typing

List = typing.List

# We don't need any special algorithms to do this. You just need to know what the transpose of a matrix looks like.
# Rows become columns and vice versa!
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])

        output = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                output[j][i] = A[i][j]
        return output

if __name__ == "__main__":
    s = Solution()
    s.transpose( [[1,2,3],[4,5,6]])