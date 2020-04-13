import collections
import typing
List = typing.List


class SolutionMy:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # flip allthe bridges
        if not A:
            return 0

        def find_first_item():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        return (i, j)

        a, b = find_first_item()
        q = collections.deque([(a, b)])

        ql = collections.deque()
        while q:
            i, j = q.popleft()
            if A[i][j] == 1:
                for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_i = i + rowOffset
                    next_j = j + colOffset
                    if 0 <= next_i < len(A) and 0 <= next_j < len(A[0]):
                        if A[next_i][next_j] == 1:
                            q.append((next_i, next_j))
                A[i][j] = 2
                ql.append((i, j, 0))
        called_times = 0
        while ql:
            called_times+=1
            a, b, level = ql.popleft()
            if A[a][b] == 1:
                print(called_times)
                return level - 1
            # marking node as visited here is too expensive
            # so, we need to mark it under the child traversal
            # if we will leave it here called_times will equal 57 for the first test case below
            #
            # A[a][b] = 2
            for xOffset, yOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = a + xOffset
                y = b + yOffset
                if 0 <= x < len(A) and 0 <= y < len(A[0]) and A[x][y] != 2:
                    ql.append((x, y, level + 1))
                    # marking node as visited here
                    # reduce amount of call
                    # called_times will be equal 27 for the first test case below
                    if A[x][y] == 0:
                        A[x][y] = 2

        return 0


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        # q = deque()
        q = set()

        def find_island():
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        traverse_island(i, j)
                        return

        def traverse_island(r, c):
            if not 0 <= r <= m - 1 or not 0 <= c <= n - 1 or A[r][c] == -1:
                return
            if A[r][c] == 1:
                A[r][c] = -1
                traverse_island(r - 1, c)
                traverse_island(r, c - 1)
                traverse_island(r + 1, c)
                traverse_island(r, c + 1)
            elif A[r][c] == 0:
                q.add((r, c, 1))

        find_island()
        # this is really interesing approach
        while q:
            temp = set()
            # r, c, d = q.popleft()
            for r, c, d in q:
                for x, y in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= x <= m - 1 and 0 <= y <= n - 1:
                        if A[x][y] == 1:
                            return d
                        elif A[x][y] == 0:
                            A[x][y] = -1
                            temp.add((x, y, d + 1))
            q = temp


if __name__ == "__main__":
    s = SolutionMy()
    s.shortestBridge([[0,1,0,0,0,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0]])
    #s.shortestBridge([[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]])

    #s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
