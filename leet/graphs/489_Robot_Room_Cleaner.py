# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None

        The key point is to return diff
        DO NOT modify the global coordinates, otherwise backtracking will not be possible
        DO NOT forget us go back
        """
        visited = set()
        cur_dir = 2

        def change_direction(direction):
            nonlocal cur_dir
            cur_dir += direction
            if cur_dir < 1:
                cur_dir = 4
            if cur_dir > 4:
                cur_dir = 1

        def get_dif():
            nonlocal cur_dir
            dx, dy = 0, 0
            if cur_dir == 1:
                dx -= 1
            elif cur_dir == 2:
                dy += 1
            elif cur_dir == 3:
                dx += 1
            elif cur_dir == 4:
                dy -= 1
            return dx, dy

        def helper(x, y):
            nonlocal cur_dir
            if (x, y) in visited:
                return
            visited.add((x, y))
            robot.clean()

            for direct in ['forward', 'left', 'right', 'back']:
                if direct == 'forward':
                    dx, dy = get_dif()
                    if (x + dx, y + dy) not in visited:
                        if robot.move():
                            helper(x + dx, y + dy)
                            robot.turnLeft()
                            robot.turnLeft()
                            change_direction(-1)
                            change_direction(-1)
                            robot.move()
                            robot.turnRight()
                            robot.turnRight()
                            change_direction(1)
                            change_direction(1)
                elif direct == 'left':
                    robot.turnLeft()
                    change_direction(-1)
                    dx, dy = get_dif()
                    if (x + dx, y + dy) in visited:
                        robot.turnRight()
                        change_direction(1)
                    else:
                        if robot.move():
                            helper(x + dx, y + dy)
                            robot.turnRight()
                            change_direction(1)
                            robot.turnRight()
                            change_direction(1)
                            robot.move()
                            robot.turnLeft()
                            change_direction(-1)
                        else:
                            robot.turnRight()
                            change_direction(1)
                elif direct == 'right':
                    robot.turnRight()
                    change_direction(1)
                    dx, dy = get_dif()
                    if (x + dx, y + dy) in visited:
                        robot.turnLeft()
                        change_direction(-1)
                    else:
                        if robot.move():
                            helper(x + dx, y + dy)
                            robot.turnLeft()
                            change_direction(-1)
                            robot.turnLeft()
                            change_direction(-1)
                            robot.move()
                            robot.turnRight()
                            change_direction(1)
                        else:
                            robot.turnLeft()
                            change_direction(-1)
                elif direct == 'back':
                    robot.turnLeft()
                    robot.turnLeft()
                    change_direction(-1)
                    change_direction(-1)
                    dx, dy = get_dif()
                    if (x + dx, y + dy) in visited:
                        robot.turnLeft()
                        robot.turnLeft()
                        change_direction(-1)
                        change_direction(-1)
                    else:
                        if robot.move():
                            helper(x + dx, y + dy)
                            robot.turnLeft()
                            robot.turnLeft()
                            robot.move()
                            change_direction(-1)
                            change_direction(-1)
                        else:
                            robot.turnLeft()
                            robot.turnLeft()
                            change_direction(-1)
                            change_direction(-1)

        helper(0, 0)

