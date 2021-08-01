b = [0] * 1000


# preprocessing needs to collect indices of the P we will return in case of mistmatch
# if P is sevsevsev, after preprocessing it returns [-1,0,0,0,1,2,3,4,5,6]
def KMP_preprocessing(text, pattern):
    m = len(pattern)
    i, j = 0, -1
    s = [0] * (m + 1)
    s[0] = -1
    while i < m:
        # once mismatch found, reset j to s[j]
        # s[j] stores the previous index of the char under pattern[j]
        # for exmaple, P is sesekl then s is [-1,0,0,1,2,0,0]
        # s[4] stores the index which is 2 of the previous e char
        while j >= 0 and pattern[j] != pattern[i]:
            j = s[j]
        i += 1
        j += 1
        s[i] = j
    return s


def KMP_search(text, pattern):
    dp = KMP_preprocessing(text, pattern)

    n = len(text)
    m = len(pattern)
    freq = 0
    i, j = 0, 0
    res = []
    while i < n:
        # once there is a mismatch
        # s[j] stores the previous index of the char under pattern[j]
        # so it moves the j pointer to the nearest previous pattern[j] match
        while j >= 0 and text[i] != pattern[j]:
            j = dp[j]
        i += 1
        j += 1
        if j == m:
            # NOTE: to find the first occurence index must use i-m
            res.append(i - m)
            freq += 1
            j = dp[j]

    print(res)
    return freq


class KMP_checking:
    def strStr(self, T: str, P: str) -> int:
        if len(P) == 0:
            return 0

        def preprocessing(P):
            m = len(P)
            i, j = 0, -1
            s = [0] * (m + 1)
            s[0] = -1
            while i < m:
                while j >= 0 and P[i] != P[j]:
                    j = s[j]
                i += 1
                j += 1
                s[i] = j
            return s

        i, j = 0, 0
        n = len(T)
        m = len(P)
        dp = preprocessing(P)
        while i < n:
            while j >= 0 and T[i] != P[j]:
                j = dp[j]
            i += 1
            j += 1
            if j == m:
                return i - m

        return -1

if __name__ == '__main__':
    s = KMP_checking()
    s.strStr("sevsevk", "pwwkew")
    s.strStr("sevsevk", "sevsek")
    s.strStr("i do not like seventy sev but seventy seventy seven", "seventy seven")
    print(KMP_search("Hello there!", "hehho"))
    print(KMP_search("Popup", "p"))
    print(KMP_search("xyzxyzxybxyb", "xyz"))
    print(KMP_search("abcd", "cdabcdab"))
    print(KMP_search("abcabcabcabc", "abcabcabcabc"))
    print(KMP_search("i do not like seventy sev but seventy seven", "seventy sevenk"))
    print(KMP_search("abcabcabcabc", "abcabcabcabc"))
