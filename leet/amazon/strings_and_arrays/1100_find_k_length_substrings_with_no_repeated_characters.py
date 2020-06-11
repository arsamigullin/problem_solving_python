class Solution1:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        d = {}
        countOfRepeatedChars = 0
        for ch in S[:K]:
            d[ch] = d.get(ch, 0) + 1
            if d[ch] - 1 == 1:
                countOfRepeatedChars += 1
        res = 0
        i, j = 0, K
        while j < len(S):
            if countOfRepeatedChars == 0:
                res += 1

            d[S[i]] -= 1
            if d[S[i]] == 1:
                countOfRepeatedChars -= 1
            elif d[S[i]] == 0:
                d.pop(S[i])

            d[S[j]] = d.get(S[j], 0) + 1
            if d[S[j]] - 1 == 1:
                countOfRepeatedChars += 1
            i += 1
            j += 1

        if countOfRepeatedChars == 0:
            res += 1
        return res


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K > len(S):
            return 0

        d = {}
        last_index = -1
        counter = 0

        for i, char in enumerate(S):
            # once the char in d
            # we update last_index with the max value between last_index and the index of the char
            # that is already in d
            # this is the left boundary for the string of len K
            if char in d:
                last_index = max(last_index, d[char])

            if i - last_index >= K:
                counter += 1

            d[char] = i

        return counter
if __name__ == '__main__':
    s = Solution()
    s.numKLenSubstrNoRepeats("abcchk",3)
