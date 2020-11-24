tests = iter(["1 8", "8 1","5 4","4 5","6 3", "8 2", "4 4", "5 5", "0 0"])
# 5 4
# 4 5
# 6 3
# 8 2
# 4 4
# 5 5
# 0 0

# 1  4 12 21 ->  71
# 1  3 11 15 32 ->  70
# 1  7 12 ->  52
# 1  5 ->  28
# 1  3 11 18 ->  44
# 1  4  9 31 51 -> 126
import collections
import itertools
def solve():
    loc_max = 0
    cur_comb = []
    _max = 0
    is_max_set = False
    def backtrack(comb, i, k, h):
        nonlocal loc_max, cur_comb, _max, is_max_set
        if len(comb) == k:
            d = collections.defaultdict(int)
            d[0] = 0
            target = 1
            while True:
                for c in comb:
                    if c <= target:
                        d[target] = min(float('inf') if target not in d else d[target], d[target - c] + 1)
                if d[target] > h:
                    break
                target += 1
            if target > loc_max:
                loc_max = target
                cur_comb = comb[:]
            else:
                if not is_max_set:
                    _max = loc_max + 1
                    is_max_set = True
            return

        if i == 1:
            comb.append(i)
            backtrack(comb, i + 1, k, h)
        else:
            while i < _max or _max == 0:
                comb.append(i)
                backtrack(comb, i + 1, k, h)
                comb.pop()
                i += 1

    while True:
        h, k = next(tests).split()
        #h, k = input().split()
        if not h or not k:
            continue
        h, k = int(h), int(k)
        if h == 0 and k == 0:
            break
        # if k == 1:
        #     print(f"{1}  -> {h}")
        #     continue

        # if h + k > 9:
        #     continue
        # if k == 0:
        #     print(f"0 -> 0")
        #     continue
        backtrack([], 1, k, h)

        print(f"{cur_comb[0]}  {' '.join(map(str, cur_comb[1:]))} -> {loc_max-1}")
        loc_max = 0
        cur_comb = []
        _max = 0
        is_max_set = False

if __name__ == '__main__':
    solve()