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
    KMP('abcdabck', 'abck')
