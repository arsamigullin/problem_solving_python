import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:

        indexdict = collections.defaultdict(list)

        prev = ''
        start = 0
        # collect intervals for each letter
        for i, ch in enumerate(text):
            if ch != prev and i != 0:
                indexdict[prev].append((start, i))
                start = i
            prev = ch
        indexdict[prev].append((start, i + 1))
        max_val = 0

        # for each letter
        for ch in indexdict:
            indices = indexdict[ch]
            n = len(indices)
            third_group_letter = n > 2
            previ, prevj = indices[0]
            max_val = max(max_val, prevj - previ)
            # for each interval
            for i in range(1, n):
                curi, curj = indices[i]
                # example aaabaaaba
                # a: (0,3) (4,6), (8,9)
                # b: (3,4),(7,8)
                # previ, prevj = 0, 2
                # curi, curj = 4, 6
                # 4-3 = 1, we will replcace this letter with the last a,
                # so this maximizes the consecutive substring length
                if curi - prevj == 1:
                    max_val = max(max_val, curj - previ + third_group_letter - 1)
                else:
                    # if gap is more one char and since n > 1 (since we are in loop that means n is definitely > 1)
                    # we grab the letter from the neighbor group
                    max_val = max(max_val, curj - curi + 1, prevj - previ + 1)
                previ, prevj = curi, curj
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