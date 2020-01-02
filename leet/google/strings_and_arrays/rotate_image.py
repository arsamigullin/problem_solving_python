#
# Observations
# 1. When rotating, we can observe that the next place
# for the current element [i,j] will be [j, len(rows) - 1]
# i.e. [i, j] => [j, len(rows) - 1]
# 3. We can rotate circle by circle starting from outer circle
#    The count of circles is always len(rows)//2
# 4. For each circle we need to rotate only
#   end_ind - start_ind or len(rows) - 1 - 2 * s1

# Algo:
#
class MySolution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) - 1
        cir_cnt = 0 # current circle to rotate

        while cir_cnt < len(matrix)//2:
            # for each circle the start position will be reduced by 1
            s1, s2 = 0 + cir_cnt, 0 + cir_cnt
            rot_cnt = m - 2 * s1 # how many items to roate in current circle
            while rot_cnt > 0:
                k = 0
                i, j = s1, s2
                tmp_out = matrix[i][j]
                while k<4:
                    tmp_in = matrix[j][m - i]
                    matrix[j][m - i] = tmp_out
                    tmp_out = tmp_in
                    i, j = j, m - i
                    k+=1
                s2+=1
                rot_cnt-=1
            cir_cnt+=1

# Another interesting approach
# we do exchange arr[i,j] with arr[j,i] and then just reverse each subarray in array
class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    s= Solution()
    s.rotate([[1,2,3],[4,5,6],[7,8,9]])
    #[[7,4,1],[8,5,2],[9,6,3]]