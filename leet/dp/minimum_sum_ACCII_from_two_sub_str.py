def solution(s1, s2):
    n = len(s1)
    m = len(s2)
    count = float('inf')
    d = dict()
    def find_min(s1, s2, n, m):
        if n >= len(s1) - 1 or m >= len(s2)- 1:
            return ""

        key = str(n) + "|" + str(m)
        if s1[n] == s2[m]:
            if key in d:
                #count = ord(s1[n]) + ord(s2[m])
                print(d[key])
                return d[key]
            else:
                d[key] = find_min(s1, s2, n + 1, m + 1) + s1[n]
                print(d[key])
                return d[key]
        else:
            if key in d:
                #count = ord(s1[n]) + ord(s2[m])
                print(d[key])
                return d[key]
            else:
                a = find_min(s1, s2, n, m + 1)
                print(a)
                b = find_min(s1, s2, n + 1, m)
                print(b)
                d[key] = a if len(a)>len(b) else b
                return d[key]


    find_min(s1,s2, 0, 0)
    print(d)


def LCSLength (s1, s2):
    l = [[0 for i in range(8)] for j in range(8)]
    #print(l)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    print(l)


if __name__ == "__main__":
    LCSLength("delete", "leet")
    solution("delete", "leet")





