from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def get_count(w):
            stack = []
            for ch in w:
                if not stack or stack[-1][0] != ch:
                    stack.append([ch, 1])
                else:
                    stack[-1][1] += 1
            return stack

        char_count_s = get_count(s)
        print(char_count_s)
        count = 0

        def get_uniq_chars(w):
            wrd = []
            for i, ch in enumerate(w):
                if not wrd or wrd[-1] != ch:
                    wrd.append(ch)
            return wrd

        char_index_s = get_uniq_chars(s)
        # print(char_index_s)
        for word in words:

            uniq_chars_word = get_uniq_chars(word)

            if uniq_chars_word != char_index_s:
                # print(word)
                break

            char_count_word = get_count(word)
            print(word)
            # print(uniq_chars_word,char_index_s)
            for i, (ch, count) in enumerate(char_count_word):
                s_count = char_count_s[i][1]
                if s_count != count and (s_count < 3 or count > s_count):
                    break
            else:
                # print(word)
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    s.expressiveWords("heeellooo", ["hello", "hi", "helo"])