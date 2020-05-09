import collections


# this is the best solution
# the corner cases we must know when dealing with khight
# 1. to reach (1,1) from (0,0) we need 2 steps
# 2. to reach (1,0) from (0,0) we need 3 steps
# 2. to reach (0,1) from (0,0) we need 3 steps

class Solution:
    '''
    we start from target point and move toward initial point
    eventually we will end up either at (0,0), (2,2), (1,0), (0,1)
    those cases we added to memo
    memo also stores the previous steps at each reached coordinate
    so we avoid a lot of calls
    '''
    def minKnightMoves(self, x, y):
        memo = {(0, 0): 0, (1, 1): 2, (1, 0): 3, (0, 1): 3}
        def dfs(x, y):
            if (x, y) in memo: return memo[(x, y)]
            # we do abs here because reaching from (0,0) to (-1,0) also takes 3 steps
            # abs will make us to grab value for (1,0)
            res = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
            memo[(x, y)] = res
            return res
        return dfs(abs(x), abs(y))



class Solution1:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [[2, 1], [2, -1], [-2, -1], [-2, 1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        q = collections.deque([(0, 0, 0)])
        visited = set()
        while q:
            i, j, step = q.popleft()
            if i == x and j == y:
                print(visited)
                return step
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for dx, dy in dirs:
                u, v = i + dx, j + dy
                if (u, v) not in visited:
                    print(f"parent {i,j}, child {u, v}")
                    q.append((u, v, step + 1))


        return 0


class Solution2:
    '''
    so, we looking for dist from 0,0 to x,y.  distance, not path.  so, it doesn't matter if x is <0 or y<0.
    we can just say the problem is x and y are both > 0.  same distance results.

    now, once we get a bit closer to x, y, our relative position changes. but the same principle holds.
    so we can update our relative position to x,y and then use only directions that's in the positive positive quadrant.
    ie, if we our relative position becomes positive, we can use, I think reflection property to change it to
    positive values again.  that is, if we're on the boundry, and one of our moves takes us to -x,
    we can just reflect it back and use positive x again, so we can always call dfs with  positive values
    '''

    def minKnightMoves(self, x: int, y: int) -> int:
        # but this is going to time out.  we're GOING to do repeated work.  so we cache it.
        def dfs(i, j):
            # we've arrived
            if i == j == 0:
                return 0
            if i + j == 2:
                # special case of 1,1 or 2,0/0,2.  it takes min 2 moves to reach those positions
                return 2
            # not special position or reached goal.  we recursively call both jumps in +x+y dir
            # and add 1
            return min(
                dfs(abs(i - 2), abs(j - 1)),
                dfs(abs(i - 1), abs(j - 2))
            ) + 1

        return dfs(abs(x), abs(y))


class Solution3:
    def minKnightMoves(self, x, y):
        memo = {(0, 0): 0, (1, 1): 2, (1, 0): 3, (0, 1): 3}
        def dfs(x, y, start):

            if (x, y) in memo: return memo[(x, y)]
            if start == 0:
                res = min(dfs(abs(x - 1), abs(y - 2), start + 1), dfs(abs(x - 2), abs(y - 1), start + 2)) + 1
            else:
                res = min(dfs(abs(x - 1), abs(y - 2), start), dfs(abs(x - 2), abs(y - 1), start), ) + 1
            memo[(x, y)] = res
            print(start, x, y, res)
            return res
        return dfs(abs(x), abs(y), 0)


class Solution4:
    def minKnightMoves(self, x: int, y: int) -> int:

        record = dict()

        # @lru_cache(None)
        def dp(x, y):
            # print(f"x{x} y:{y}")

            if x + y == 0:
                return 0

            if x + y == 2:
                return 2

            if (x, y) in record:
                return record[(x, y)]

            value = min(dp(abs(x - 1), abs(y - 2)), dp(abs(x - 2), abs(y - 1))) + 1
            record[(x, y)] = value

            return value

        return dp(abs(x), abs(y))


class Solution5:
    def minKnightMoves(self, x: int, y: int) -> int:

        steps = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

        x, y = abs(x), abs(y)
        ans = 0
        while x > 4 or y > 4:
            ans += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2

        queue = collections.deque([(0, 0, 0)])

        while queue:
            i, j, step = queue.popleft()

            if x == i and y == j:
                return ans + step

            for di, dj in steps:
                if (x - i) * di > 0 or (y - j) * dj > 0:
                    queue.append((i + di, j + dj, step + 1))

class Solution6:
    def minKnightMoves(self, x: int, y: int) -> int:

        steps = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

        x, y = abs(x), abs(y)
        ans = 0

        queue = collections.deque([(0, 0, 0)])

        while queue:
            i, j, step = queue.popleft()

            if x == i and y == j:
                return ans + step
            for di, dj in steps:
                if (x - i) * di > 0 or (y - j) * dj > 0:
                    queue.append((i + di, j + dj, step + 1))

if __name__ == '__main__':
    s = Solution5()
    s.minKnightMoves(10, 10)
