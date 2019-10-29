def LCSLength(s1, s2):
    l = [[0 for i in range(8)] for j in range(8)]
    # print(l)
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    return l


global lookup
lookup = []

def LCS(s1, s2, n, m, ):
    if n == 0 and m == 0:
        return ""
    if s1[n-1] == s2[m-1]:
        seq_list = LCS(s1, s2, n-1, m-1)

        for s in seq_list:




if __name__ == "__main__":
    s1 = "delete"
    s2 = "leet"
    lookup = LCSLength(s1, s2)
    print(LCS(s1, s2, len(s1), len(s2)))
    #solution("delete", "leet")
