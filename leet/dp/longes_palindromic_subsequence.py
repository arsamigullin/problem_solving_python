def solution(s):
    d = dict()
    def find(i,j):
        if i>j:
            return 0
        if i==j:
            return 1
        if s[i] == s[j]:
            return find(i+1, j-1) + 2
        key = str(i)+"|"+str(j)
        if key not in d:
            d[key] = max(find(i+1,j), find(i,j-1))
        return d[key]
    return find(0, len(s) - 1)

if __name__ == "__main__":
    print(solution("bbbab"))