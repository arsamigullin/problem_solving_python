from typing import List
# diagonal length

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        i, j, di, dj = 0, 0, 0, 1
        direction = 0
        res = [0] * (m * n)
        l = 0
        while l < m * n:
            # this is diagonal length
            cnt = min(j + 1, n - i)
            x, y = i, j
            rng = range(cnt) if direction == 1 else range(cnt)[::-1]
            for k in rng:
                res[l + k] = matrix[x][y]
                x += 1
                y -= 1
            matrix[i][j] = None
            # this is how we go over the top and right border
            if matrix[(i + di) % n][(j + dj) % m] is None:
                di, dj = dj, di
            i += di
            j += dj
            direction ^= 1
            l += cnt
        return res

# this is solution with reverse
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n = len(matrix)
        m = len(matrix[0])
        length = n + m - 1
        i = 0
        j = 0
        direction = 0
        di, dj = 0, 1
        res = []
        l = 0
        while l < length:
            x, y = i, j
            arr = []
            while 0<=x<n and 0<=y<m:
                arr.append(matrix[x][y])
                x+=1
                y-=1
            if direction == 0:
                arr = arr[::-1]
            res.extend(arr)
            matrix[i][j] = None
            if matrix[(i + di) % n][(j + dj) % m] == None:
                di, dj = dj, di
            i += di
            j += dj
            direction ^= 1
            l+=1
        return res

if __name__ == '__main__':
    s = Solution()
    s.findDiagonalOrder([[2,5],[8,4],[0,-1]])
    s.findDiagonalOrder([[3],[2]])
    s.findDiagonalOrder([[2,3]])
    s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])