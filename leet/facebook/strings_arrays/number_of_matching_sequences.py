# fast solution
class Solution(object):
    def numMatchingSubseq(self, S, words):
        ans = 0
        heads = [[] for _ in range(26)]
        for word in words:
            # read more about iter
            # https://docs.python.org/3.8/library/functions.html?highlight=iter#iter
            it = iter(word)
            #print(next(it))
            heads[ord(next(it)) - ord('a')].append(it)

        for letter in S:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1

        return ans


import collections


class SolutionWithoutIterators:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        ans = 0

        headers = collections.defaultdict(list)
        for word_idx in range(len(words)):
            headers[words[word_idx][0]].append((word_idx, 1))

        for letter in S:
            if letter in headers:
                stack = headers[letter]
                headers[letter] = []
                while stack:
                    word_idx, next_letter_idx = stack.pop()
                    if next_letter_idx == len(words[word_idx]):
                        ans += 1
                    else:
                        headers[words[word_idx][next_letter_idx]].append((word_idx, next_letter_idx + 1))

        return ans


if __name__ == "__main__":
    s = Solution()
    s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])

# the fatest solution
# next array technique
# For each char in source we store array[26] that stores indexes
# for example, the source 'abc' with 0,1,2 indexes accordingly
# we create arr(len(source)) and starting form the end of source we populate arr
# with array[26] where we put index to the char location
#[
#    [0, 1, 2...],
#    [-1, 1, 2...],
#    [-1, -1, 2...]
#]
class MySolution:
    def numMatchingSubseq(self, S: str, words: list) -> int:
        narr = self.__nexarr(S)
        cnt = 0

        for word in words:
            i = 0
            for ch in word:
                # NOTE: we start from i = 0
                # if we found the char we jump to the next to this char position (iNex+1) position
                # Once we exceeded i we return -1
                index = narr[i][ord(ch) - ord('a')] if i < len(S) else -1
                if index == -1:
                    cnt -= 1
                    break
                else:
                    i = index + 1
            cnt += 1
        return cnt

    def __nexarr(self, source):
        result = [None] * len(source)
        current = [-1] * 26
        for i in range(len(source))[::-1]:
            current[ord(source[i]) - ord('a')] = i
            result[i] = current[:]
        return result


