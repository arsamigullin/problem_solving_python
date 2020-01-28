# python reverse
# we start from beginning and count D (represents decreasing order)
# once the next symbol is I we reverse subarray(with the len of found D) of seq array
class Solution:
    def findPermutation(self, s: str) -> list:

        seq = [i for i in range(1, len(s) + 2)]
        # print(seq)
        i = 0
        dcnt = 0
        while i < len(s):
            if s[i] == 'D':
                dcnt += 1
                if i == len(s) - 1:
                    i += 1
                    seq[i - dcnt:i + 1] = seq[i - dcnt: i + 1][::-1]
            else:
                seq[i - dcnt:i + 1] = seq[i - dcnt: i + 1][::-1]
                # print(i-dcnt, i + 1)
                dcnt = 0
            i += 1

        return seq

# this is the same but reverse is manual
class Solution:
    def findPermutation(self, s: str) -> list:

        seq = [i for i in range(1, len(s) + 2)]
        i = 0
        dcnt = 0

        def reverse(arr, start, end):
            i = 0
            while i < (end - start) // 2:
                arr[i + start], arr[end - i - 1] = arr[end - i - 1], arr[i + start]
                i += 1

        while i < len(s):
            if s[i] == 'D':
                dcnt += 1
                if i == len(s) - 1:
                    i += 1
                    reverse(seq, i - dcnt, i + 1)
            else:
                reverse(seq, i - dcnt, i + 1)
                dcnt = 0
            i += 1

        return seq


import re


class Solution:

    # https://leetcode.com/problems/find-permutation/discuss/96624/1-liner-and-5-liner-visual-explanation
    # If it's all just I, then the answer is the numbers in ascending order.
    # And if there are streaks of D, then just reverse the number streak under each:
    # def findPermutation(self, s):
    #     a = range(1, len(s) + 2)
    #     for m in re.finditer('D+', s):
    #         i, j = m.start(), m.end() + 1
    #         a[i:j] = a[i:j][::-1]
    #     return a

    def findPermutation(self, s: str) -> list:
        sols = list(range(1, len(s) + 2))
        for m in re.finditer(r"D+", s):
            s, e = m.start(), m.end() + 1
            sols[s:e] = sols[s:e][::-1]
        return sols