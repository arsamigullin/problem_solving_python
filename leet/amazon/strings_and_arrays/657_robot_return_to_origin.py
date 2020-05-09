class Solution:
    def judgeCircle(self, moves: str) -> bool:

        x, y = 0, 0
        d = {'U': 1, 'D': -1, 'L': -1, 'R': 1}
        for ch in moves:
            if ch in ('L', 'R'):
                x += d[ch]
            if ch in ('U', 'D'):
                y += d[ch]
        return x == 0 and y == 0



class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')