class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        c = {ch:i for i, ch in enumerate(keyboard)}
        prev = 0
        tot = 0
        for ch in word:
            tot+=abs(prev-c[ch])
            prev= c[ch]
        return tot

