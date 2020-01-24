# Algo
# Although nowhere has been said that the order should be the same
# 1. We must sort the strings with len key. Otherwise we will get incorrect result
# Suppose words = [sdfgsf,s,f], So the word sdfgsf will have incorrect count
# 2. Construct dictionary where keys are words
# 3. We will remove one char from word for each word in words. After each removing a char
# we check if a new string (without the removed char) is in dictionary
# and if it is we take max length of the chain at that word
#

class Solution:
    def longestStrChain(self, words: list) -> int:
        d = {word: 1 for word in words}
        longest = 1
        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in d:
                    d[word] = max(d[word], d[prev] + 1)
            longest = max(longest, d[word])
        return longest





# TLE
class Solution:
    def longestStrChain(self, words: list) -> int:
        word_cnt = [[0] * 26 for _ in range(len(words))]
        for i, word in enumerate(words):
            for j, c in enumerate(word):
                word_cnt[i][ord(c) - 97] += 1

        def find(s, last):
            if s >= len(words):
                return [last]
            cnt, ans = 0, []
            for i in range(s, len(words)):
                for j in range(s - 1, i):
                    diff = find_diff(word_cnt[j], word_cnt[i])
                    if diff == 1:
                        res = find(i + 1)
                        res.append(words[j])
                        if len(res) > cnt:
                            cnt = len(res)
                            ans = res
            return ans

        def find_diff(a, b):
            if abs(len(a) - len(b)) > 1:
                return 2
            return sum(abs(x - y) for x, y in zip(a, b))

        return find(1)


if __name__ == "__main__":
    s = Solution()
    s.longestStrChain(["a","b","ba","bca","bda","bdca"])