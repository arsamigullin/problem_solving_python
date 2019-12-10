def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ds = {}
    dt = {}
    for c in s:
        if c not in ds:
            ds[c] = 1
        else:
            ds[c] += 1
    for c  in t:
        if c not in dt:
            dt[c] = 1
        else:
            dt[c] += 1

    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] in dt:
            if ds[s[i]] - 1 >= dt[s[i]]:
                ds[s[i]] -= 1
                i += 1
            else:
                break
        else:
            i += 1

    while i <= j:
        if s[j] in dt:
            if ds[s[j]] - 1 >= dt[s[j]]:
                ds[s[j]] -= 1
                j -= 1
            else:
                break
        else:
            j -= 1

    return s[i:j+1]



if __name__ == "__main__":
    #print(minWindow("a", "b"))
    print(minWindow("cabwefgewcwaefgcf","cae"))