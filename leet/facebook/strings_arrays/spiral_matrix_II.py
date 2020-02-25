# here we have directions queue
# 0 right
# 1 down
# 2 left
# 4 up
# once direction is changed we change row/col and setting up new direction
import collections
import typing
List = typing.List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = collections.deque([0, 1, 2, 3])
        result = [[0] * n for _ in range(n)]
        direction = directions.popleft()
        directions.append(direction)
        i, j = 0, 0

        for d in range(1, n**2 + 1):
            dir_changed = False
            result[i][j] = d
            if direction == 0:
                if j + 1 >= n or result[i][j + 1] != 0:
                    dir_changed = True
                    i+=1
                else:
                    j += 1
            elif direction == 1:
                if i + 1>= n or result[i + 1][j] != 0:
                    dir_changed = True
                    j -= 1
                else:
                    i += 1

            elif direction == 2:
                if j - 1 < 0 or result[i][j - 1] != 0:
                    dir_changed = True
                    i -= 1
                else:
                    j-=1

            elif direction == 3:
                if i - 1 < 0 or result[i - 1][j] != 0:
                    dir_changed = True
                    j += 1
                else:
                    i-=1

            if dir_changed:
                direction = directions.popleft()
                directions.append(direction)
        return result


class SolutionShort:
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
# n = 9
# iteration1
# A[0][0] = 1
# i1 =(i+di)%n = (0+0)%n = 0
# j1 =(j+dj)%n = (0+1)%n = 1
# if A[i1][j1] is False since A[0][1] is 0
# i = i + di = 0 + 0 = 0
# j = j + dj = 0 + 1 = 1 # note column moved forward

# iteration 2
# A[0][1] = 2
# i1 = (i+di)%n = (0+0)%n = 0
# j1 =(j+dj)%n = (1+1)%n = 2
# if A[i1][j1] is False since A[0][2] is 0
# i = i + di = 0 + 0 = 0
# j = j + dj = 1 + 1 = 2 # note column moved forward

# iteration 2
# A[0][2] = 2
# i1 = (i+di)%n = (0+0)%n = 0
# j1 =(j+dj)%n = (2+1)%n = 3%3 = 0
# if A[i1][j1] is True since A[0][0] is 1
# we swap di and dj
# di = dj = 1 dj = -di = 0
# i = i + di = 0 + 1 = 1
# j = j + dj = 2 - 0  = 2

# iteration 3
# A[1][2] = 4
# i1 = (i+di)%n = (1+0)%n = 0
# j1 =(j+dj)%n = (2+0)%n = 2%3 = 2
# if A[i1][j1] is False since A[2][2] is 0
# i = i + di = 0 + 1 = 1
# j = j + dj = 2 - 0  = 2

if __name__ == "__main__":
    s = SolutionShort()
    s.generateMatrix(3)