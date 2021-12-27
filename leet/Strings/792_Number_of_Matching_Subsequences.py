import bisect
import collections
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        heads = [[] for _ in range(26)]
        for w in words:
            # this is an iterator of the word
            it = iter(w)
            # we are grouping the words by their first letter and we put left letters in the iterator it
            heads[ord(next(it)) - ord('a')].append(it)

        # print(heads)
        ans = 0
        for i, letter in enumerate(s):
            # now we've got the index for the heads array
            head_index = ord(letter) - ord('a')
            old_bucket = heads[head_index]
            # and resetting the bucket
            heads[head_index] = []


            while old_bucket:
                #  here we've just popping words from the old_bucket
                cur_word = old_bucket.pop()
                # getting key of the bucket we want to put the left letters of the cur_word (which is iter) in
                nxt = next(cur_word, None)
                if nxt:
                    # put the left letters to the bucket determined by the first letter
                    heads[ord(nxt) - ord('a')].append(cur_word)
                else:
                    ans+=1
        return ans


class Solution1:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        ind = collections.defaultdict(list)
        for i, ch in enumerate(s):
            ind[ch].append(i)
        cnt = 0

        def bisect_right(arr, targ):
            lo = 0
            hi = len(arr)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if targ < arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        for word in words:
            target = -1
            for ch in word:
                i = bisect_right(ind[ch], target)
                if i >= len(ind[ch]):
                    break
                target = ind[ch][i]
            else:
                cnt += 1
        return cnt

class Solution3:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        heads = [[] for _ in range(26)]
        for w in words:
            # we are grouping the words by their first letter and we put left letters in the iterator it
            heads[ord(w[0]) - ord('a')].append((1,w))

        # print(heads)
        ans = 0
        for i, letter in enumerate(s):
            head_index = ord(letter) - ord('a')
            old_bucket = heads[head_index]
            heads[head_index] = []


            while old_bucket:
                i, word = old_bucket.pop()
                if i<len(word):
                    heads[ord(word[i]) - ord('a')].append((i+1, word))
                else:
                    ans+=1
        return ans


if __name__ == '__main__':
    s = Solution3()
    s.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"])
    s.numMatchingSubseq("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])
