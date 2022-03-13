import collections
from itertools import groupby

class Solution:
    def maxRepOpt1(self, text: str) -> int:

        intervals = collections.defaultdict(list)
        #gb = list(groupby(text))
        prev = ''
        start = 0
        # collect intervals for each letter
        for i, ch in enumerate(text):
            if ch != prev and i != 0:
                intervals[prev].append((start, i))
                start = i
            prev = ch
        intervals[prev].append((start, i + 1))
        max_val = 0

        # for each letter
        for ch in intervals:
            indices = intervals[ch]
            n = len(indices)
            third_interval_letter = n > 2
            previ, prevj = indices[0]
            max_val = max(max_val, prevj - previ)
            # for each interval
            for i in range(1, n):
                curi, curj = indices[i]
                # example aaabaaaba, intervals are
                # a: (0,3) (4,6), (8,9)
                # b: (3,4),(7,8)
                # previ, prevj = 0, 2
                # curi, curj = 4, 6
                # curi - prevj = 4-3 = 1, we replace this letter with the last a
                # (note: last letter is from the third interval)
                # so this maximizes the consecutive substring length with the same letter
                if curi - prevj == 1:
                    max_val = max(max_val, curj - previ + third_interval_letter - 1)
                else:
                    # if gap is more one char and since n > 1 (since we are inside of the loop that means n is definitely > 1)
                    # we grab the letter from the neighbor interval for prev and current intervals
                    max_val = max(max_val, curj - curi + 1, prevj - previ + 1)
                previ, prevj = curi, curj
        return max_val

# more readable
class Solution:
    def maxRepOpt1(self, text: str) -> int:

        intervals = collections.defaultdict(list)
        n = len(text)
        i = 0
        while i < n:
            ch = text[i]
            j = i
            while j < n and text[j] == ch:
                j += 1
            intervals[ch].append((i, j))
            i = j
        max_val = 0

        for ch, intvals in intervals.items():
            cur_start, cur_end = intvals[0]
            third_interval_exists = len(intvals) > 2
            max_val = max(max_val, cur_end - cur_start)
            for j in range(1, len(intvals)):
                next_start, next_end = intvals[j]
                if next_start - cur_end == 1:
                    max_val = max(max_val, next_end - cur_start + third_interval_exists - 1)
                else:
                    max_val = max(max_val, cur_end - cur_start + 1, next_end - next_start + 1)
                cur_start, cur_end = next_start, next_end
        return max_val


if __name__ == '__main__':
    s = Solution()
    s.maxRepOpt1("aaabbaaa")
    s.maxRepOpt1("aabaaa")
    s.maxRepOpt1("abc")
    s.maxRepOpt1("abcaaa")


    s.maxRepOpt1("aaaaa")
    s.maxRepOpt1("aaabbaaa")

    #"laidjgffgkapodfodlldoooehghhfdsdcvvvccuufdo"
    #"aabaaabaaaba"