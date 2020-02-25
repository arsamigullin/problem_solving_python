import typing
List = typing.List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        i, j, id, jd = 0,0,0,1
        rows = len(matrix)
        cols = len(matrix[0])
        for _ in range(rows * cols):
            res.append(matrix[i][j])
            matrix[i][j] = float('-inf')
            if matrix[(i+id)%rows][(j+jd)%cols] == float('-inf'):
                id, jd = jd, -id
            i+=id
            j+=jd
        return res
if __name__ == "__main__":
    s = Solution()
    s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

