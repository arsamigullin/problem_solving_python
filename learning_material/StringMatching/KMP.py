
b = [0] * 1000

def kmpPreprocess(P):
  global b

  m = len(P)

  i, j = 0, -1
  b[0] = -1
  while i < m:
    while j >= 0 and P[i] != P[j]:
      j = b[j]
    i += 1
    j += 1
    b[i] = j


def kmpSearch(T, P):
  global b
  kmpPreprocess(P)
  n = len(T)
  m = len(P)

  freq = 0
  i, j = 0, 0
  while i < n:
    while j >= 0 and T[i] != P[j]:
      j = b[j]
    i += 1
    j += 1
    if j == m:
      freq += 1
      j = b[j]
  return freq


def KMP_preprocessing(text, pattern):
    m = len(pattern)
    n = len(text)
    i, j = 0, -1
    s = [0] * (m+1)
    s[0] = -1
    while i < m:
        while j>=0 and pattern[j]!=pattern[i]:
            j = s[j]
        i+=1
        j+=1
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
        while j>=0 and text[i]!=pattern[j]:
            j = dp[j]
        i+=1
        j+=1
        if j == m:
            res.append(i - m)
            freq+=1
            j = dp[j]

    print(res)
    return freq









def get_pref_table(pattern):
    n = len(pattern)
    s = [0] * n
    j = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[j]:
            s[i] = j + 1
            j += 1
            i += 1
        else:
            if j > 0:
                j = s[j - 1]
            else:
                s[i] = 0
                i += 1
    return s

def KMP(text, pattern):
    s = get_pref_table(pattern)
    m = len(text)
    n = len(pattern)
    i = 0
    j = 0
    while i<m:
        if pattern[j] == text[i]:
            i+=1
            j+=1
        if j == n:
            return i - j
        if i < m and pattern[j] != text[i]:
            if j > 0:
                j = s[j - 1]
            else:
                i+=1

if __name__ == '__main__':
    print(KMP_search("Hello there!", "helo"))
    print(KMP_search("Popup", "p"))
    print(KMP_search("xyzxyzxybxyb", "xyz"))
    print(KMP_search("abcd","cdabcdab"))
    print(KMP_search("abcabcabcabc","abcabcabcabc"))
    print(KMP_search("i do not like seventy sev but seventy seven", "seventy sevenk"))
    print(KMP_search("abcabcabcabc", "abcabcabcabc"))
    print(kmpSearch("i do not like seventy sev but seventy seven", "seventy seven"))

    print(KMP("i do not like seventy sev but seventy seven", "seventy seven"))
