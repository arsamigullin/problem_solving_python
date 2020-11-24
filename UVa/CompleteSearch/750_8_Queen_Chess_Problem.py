# tsts = iter(['1','','1 1'])
# tsts = iter(['4','','1 2','','6 7','','7 8','','8 8'])
tsts = iter(['64','','1 1','','1 2','','1 3','','1 4','','1 5','','1 6','','1 7','','1 8','','2 1','','2 2','','2 3','','2 4','','2 5','','2 6','','2 7','','2 8','','3 1','','3 2','','3 3','','3 4','','3 5','','3 6','','3 7','','3 8','','4 1','','4 2','','4 3','','4 4','','4 5','','4 6','','4 7','','4 8','','5 1','','5 2','','5 3','','5 4','','5 5','','5 6','','5 7','','5 8','','6 1','','6 2','','6 3','','6 4','','6 5','','6 6','','6 7','','6 8','','7 1','','7 2','','7 3','','7 4','','7 5','','7 6','','7 7','','7 8','','8 1','','8 2','','8 3','','8 4','','8 5','','8 6','','8 7','','8 8'])
#tsts = iter(['6', '1 2', '3 4', '6 1', '2 7', '5 5', '4 2'])

############## My solution ###########
def check_diag(i, j, hill, dale):
    if i - j in dale:
        return False
    if i + j in hill:
        return False
    return True


def main():
    n = int(input())
    #n = int(next(tsts))
    tests = []
    while n > 0:
        inp = input()
        #inp = next(tsts)
        if inp:
            tests.append(map(int, inp.split()))
            n -= 1
        else:
            continue

    for p, (x, y) in enumerate(tests):
        x, y = x - 1, y - 1
        board = [[0] * 8 for _ in range(8)]
        board[x][y] = 1
        rows = [0] * 8
        rows[x] = 1
        cols = [0] * 8
        cols[y] = 1

        hill = set()
        hill.add(x + y)
        dale = set()
        dale.add(x - y)
        print("SOLN       COLUMN")
        print(f" #      {' '.join(map(str, range(1, 9)))}")
        print()
        result = []

        def helper(xe, ye, i, k):
            if i >= 8:
                res = [0] * 8
                for u in range(8):
                    for v in range(8):
                        if board[v][u] == 1:
                            res[u] = v + 1
                result.append(res)
                return
            for j in range(k, 8):
                if i == xe and j == ye:
                    helper(8, 8, i + 1, 0)
                    return
                else:
                    if rows[i] == 0 and cols[j] == 0 and check_diag(i, j, hill, dale):
                        rows[i] = 1
                        cols[j] = 1
                        hill.add(i + j)
                        dale.add(i - j)
                        board[i][j] = 1
                        helper(xe, ye, i + 1, 0)
                        rows[i] -= 1
                        cols[j] -= 1
                        board[i][j] = 0
                        hill.discard(i + j)
                        dale.discard(i - j)

        helper(x, y, 0, 0)
        for l, r in enumerate(sorted(result)):
            print(f"{' ' + str(l + 1) if l + 1 < 10 else l + 1}      {' '.join(map(str, r))}")
        if p != len(tests)-1:
            print()

############# Steven's solution ####################
def canPlace(r, c):
    for prev in range(c):
        if row[prev] == r or abs(row[prev]-r) == abs(prev-c):
            return False
    return True

def backtrack(c):
    global lineCounter
    # we go over all the options but at the end we see
    # if row[b] is filled with a (which is a problem's requirement)
    if c == 8 and row[b] == a:
        lineCounter += 1
        print("%2d     " % lineCounter, *[i+1 for i in row])
        return
    for r in range(8):
        # this check is to make sure that at column b we will place row a (which is a problem's requirement)
        # in  other words we do not want to place to column b any row but a
        if c == b and r != a:
            continue
        if canPlace(r, c):
            row[c] = r
            backtrack(c+1)

for tc in range(int(input())):
    if tc > 0:
        print()
    input()
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    row = [0] * 8
    lineCounter = 0
    print("SOLN       COLUMN")
    print(" #      1 2 3 4 5 6 7 8\n")
    backtrack(0)

if __name__ == '__main__':
    main()
