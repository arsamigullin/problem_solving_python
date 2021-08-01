import collections


class Solution1:
    def maxRepOpt1(self, text: str) -> int:

        def helper(txt):
            d = {}
            continious = {}
            max_continious = {}
            for i, ch in enumerate(txt):
                if ch not in d:
                    d[ch] = (i, -1, 0, i, 1)
                    continious[ch] = 1
                else:
                    start, wantToReplace, countDiff, latest, length = d[ch]
                    if wantToReplace >= 0:
                        length = max(wantToReplace, latest) - start + 1
                        if countDiff == 1:
                            latest = i
                    else:
                        latest = i
                        length += 1
                    d[ch] = (start, wantToReplace, countDiff, latest, length)

                if i == 0:
                    continue
                prev = txt[i - 1]
                if prev == ch:
                    continious[ch]+=1
                else:
                    max_continious[prev] = max(max_continious.get(prev,1), continious[prev])
                    max_continious[ch] = max(max_continious.get(ch, 1), continious[ch])
                    continious[ch] = 1
                for char, (start, wantToReplace, countDiff, latest, length) in d.items():
                    if char != ch:
                        countDiff += 1
                        if countDiff == 1:
                            wantToReplace = i
                        d[char] = (start, wantToReplace, countDiff, latest, length)
            _max = 0
            for ch, cnt in continious.items():
                _max = max(_max, max(cnt, d[ch][4]), max_continious[ch])
            return _max

        forw = helper(text)
        backw = helper(text[::-1])

        return max(backw, forw)


class Solution:
    def maxRepOpt1(self, text: str) -> int:

        left = {}
        REPLACE = 0
        LEAVE_AS_IT_IS = -1
        res, i, n = 1, 0, 0
        inuse = collections.defaultdict(int)

        for ch in text:
            left[ch] = left.get(ch, 0) + 1

        for j, ch in enumerate(text):
            inuse[ch] += 1
            left[ch] -= 1
            n = max(inuse[ch],n)

            action = j - i - n

            if action >= 1:
                inuse[text[i]] -= 1
                left[text[i]] += 1
                i += 1

            char_exists = False
            if action == REPLACE:
                char_exists = left[ch] > 0
            elif action == LEAVE_AS_IT_IS:
                char_exists = True

            if char_exists and j - i >= res:
                res = j - i + 1

        return res


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        inuse = collections.defaultdict(int)  # chars used in the repeated substring
        left = {}  # not used chars
        MOVE_TO_THE_NEXT_CHAR = 1
        REPLACE = 0
        LEAVE_AS_IT_IS = -1
        res, i, n = 1, 0, 0

        # initially no chars are used yet
        for ch in text:
            left[ch] = left.get(ch, 0) + 1

        for j, ch in enumerate(text):
            inuse[ch] += 1  # since we use this char
            left[ch] -= 1  # subtract its count from left dict
            n = max(inuse[ch], n)

            # this defines action we are going to take
            action = j - i - n

            char_exists = False
            if action >= MOVE_TO_THE_NEXT_CHAR:
                inuse[text[i]] -= 1
                left[text[i]] += 1  # add it to the left since it is no
                i += 1
            elif action == REPLACE:
                char_exists = left[ch] > 0
            elif action == LEAVE_AS_IT_IS:
                char_exists = True

            if char_exists and j - i >= res:
                res = j - i + 1

        return res

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        text += ' '
        mx, ct, l = 1, collections.Counter(text), len(text)
        st = i = 0
        while i < l:
            if text[i] != text[st]:
                j = i+1
                while j < l and text[j] == text[st]: j+=1
                count = j-st-1
                if count < ct[text[st]]: count += 1
                mx = max(mx, count)
                st = i
            i += 1
        return mx

if __name__ == '__main__':
    s = Solution()
    s.maxRepOpt1("abc")
    s.maxRepOpt1("abcaaa")


    s.maxRepOpt1("aaaaa")
    s.maxRepOpt1("aaabbaaa")

    #"laidjgffgkapodfodlldoooehghhfdsdcvvvccuufdo"
    #"aabaaabaaaba"