class Solution1:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_dir = 1

        def change_dir(direction):
            nonlocal cur_dir

            if direction == 'L':
                cur_dir += 1
            else:
                cur_dir -= 1
            if cur_dir == -1:
                cur_dir = 3
            if cur_dir == 4:
                cur_dir = 0

        def get_diff():
            if cur_dir == 1:
                return 0, 1
            elif cur_dir == 2:
                return -1, 0
            elif cur_dir == 3:
                return 0, -1
            else:
                return 1, 0

        x, y = 0, 0
        for i, instr in enumerate(instructions * 4):
            if instr == 'G':
                dx, dy = get_diff()
                x += dx
                y += dy
                if x == 0 and y == 0:
                    return True
            else:
                change_dir(instr)
        return False


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0

        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0

if __name__ == '__main__':
    s = Solution()
    s.isRobotBounded("GLGLGGLGL")