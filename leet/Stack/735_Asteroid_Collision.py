from typing import List
import bisect

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            if a < 0:
                if not stack or stack[-1] < 0:
                    stack.append(a)
                else:
                    while stack and stack[-1] > 0:
                        if stack[-1] == abs(a):
                            stack.pop()
                            break
                        elif stack[-1] > abs(a):
                            break
                        elif stack[-1] < abs(a):
                            stack.pop()
                    else:
                        stack.append(a)
            else:
                stack.append(a)
        return stack


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] == abs(asteroids[i]):
                    stack.pop()
                    break
                elif stack[-1] < abs(asteroids[i]):
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroids[i])
        return stack

