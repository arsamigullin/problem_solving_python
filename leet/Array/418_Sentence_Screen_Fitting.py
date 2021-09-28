from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:

        count = 0
        lens = [len(word) for word in sentence]
        whole_sentence = sum(lens) + len(sentence) - 1
        print(whole_sentence)
        j = 0
        for i in range(rows):
            col = cols
            if j > 0:
                left_words = sum(lens[j:])
                white_spaces = len(lens) - j - 1
                col -= (left_words + white_spaces + 1)
                count += 1
                j = 0

            whole, rem = divmod(col, whole_sentence)
            count += whole
            if whole > 0:
                rem -= 1
            cur = 0
            while j < len(lens):
                if cur + lens[j] > rem:
                    break
                cur += lens[j] + 1
                j += 1
            else:
                j = 0
        return count

if __name__ == '__main__':
    s = Solution()
    s.wordsTyping(["i","had","apple","pie"], 4, 5)