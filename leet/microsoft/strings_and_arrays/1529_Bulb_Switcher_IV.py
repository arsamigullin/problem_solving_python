class Solution:
    def minFlips(self, target: str) -> int:
        flips, b = 0, 1
        for c in target:
            if int(c) == b:
                flips += 1
                b = 1 - b
        return flips