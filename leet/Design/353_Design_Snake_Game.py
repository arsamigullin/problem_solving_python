import collections
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.n = height
        self.m = width
        self.dirs = {'L': [0, -1], 'U': [-1, 0], 'R': [0, 1], 'D': [1, 0]}
        self.food = collections.deque(food)
        self.snake_set = {(0, 0)}
        self.snake = collections.deque([(0, 0)])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.snake[-1][0] + self.dirs[direction][0], self.snake[-1][1] + self.dirs[direction][1]
        # print(x,y)
        # went out bound
        if x >= self.n or y >= self.m or x < 0 or y < 0:
            return -1
        tail = self.snake.popleft()
        self.snake_set.discard(tail)
        if (x, y) in self.snake_set:
            return -1

        if len(self.food) > 0 and (x, y) == (self.food[0][0], self.food[0][1]):
            self.food.popleft()
            self.snake.appendleft(tail)
            self.snake_set.add(tail)
        self.snake.append((x, y))
        self.snake_set.add((x, y))

        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)