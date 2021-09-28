from typing import List


class Solution:
    def wordsTyping(self, words: List[str], rows: int, cols: int) -> int:
        sentence = ' '.join(words) + ' '
        sentence_length = len(sentence)
        used_cells = 0
        # used_cells are cells we used in the 2D array
        for i in range(rows):
            used_cells += cols
            # this way we exploring the left side neighbors
            while sentence[used_cells % sentence_length] != ' ':
                used_cells -= 1
            used_cells += 1 # compensate the whitespace
        # used_cells are not necessarily equally divisible to sentence_length,
        # we only want to fit the full sentences
        return used_cells // sentence_length

if __name__ == '__main__':
    s = Solution()
    s.wordsTyping(["a","bcd","e"],3,6)
