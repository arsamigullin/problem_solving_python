def cut_rod(prices,n):
    if n == 1:
        return 0
    q = -1
    for i in range(1, n):
        q = max(q, prices[i] + cut_rod(prices, n - i))
    print(q)
    return q

def solution_bottom_up(p):
    n = len(p)
    revenue = [0] * (n+1)
    for j in range(n):
        q = 0
        for i in range(j+1):
            q = max(q, p[i] + revenue[j-i])
        revenue[j+1] = q
    return revenue[n]

def solution_bottom_up_with_first_cut(p):
    n = len(p)
    s = [0]* (n+1)
    revenue = [0] * (n+1)
    for j in range(n):
        q = 0
        for i in range(j+1):
            if q < p[i] + revenue[j-i]:
                q = p[i] + revenue[j-i]
                s[j] = i
        revenue[j+1] = q

    for i in range(n+1):
        print(s[i], n -s[i], revenue[i], '| ')

    return revenue[n]

if __name__ == "__main__":
    prs = [0, 1,5,8,9,10,17,17,20,24,30]
    print(cut_rod(prs, len(prs)))
    print(solution_bottom_up_with_first_cut(prs))
    print(solution_bottom_up(prs))
