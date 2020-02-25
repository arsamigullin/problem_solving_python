import typing
List = typing.List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        """
        Do not return anything, modify rooms in-place instead.
        """
        m = 2147483647

        def find(i, j, d):
            if rooms[i][j] < d:
                return
            rooms[i][j] = min(rooms[i][j], d)
            for rowOffset, colOffset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ci, cj = i + rowOffset, j + colOffset
                if 0 <= ci < len(rooms) and 0 <= cj < len(rooms[0]):
                    find(ci, cj, d + 1)

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    find(i, j, 0)
if __name__ =="__main__":
    s = Solution()
    s.wallsAndGates([[2147483647, -1,           0,         2147483647],
                     [2147483647, 2147483647,  2147483647,      -1],
                     [2147483647, -1,          2147483647,      -1],
                     [0,          -1,          2147483647, 2147483647]])