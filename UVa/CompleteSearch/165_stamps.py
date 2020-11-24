import itertools




# 5 4
# 4 5
# 6 3
# 8 2
# 4 4
# 5 5
# 0 0

def main():
    while True:
        # h, k = map(int, input().split())
        h, k = map(int, next(tests).split())
        if h == 0 and k == 0:
            break

        if k == 1:
            print(h)
            continue

        _max = float('-inf')
        n = 3
        cache = {}
        max_comb = None
        for i in range(1, k + 1):
            while True:
                loc_max = float('-inf')
                combs = list(itertools.combinations(range(2, n), i))
                if not combs:
                    break
                dp = {}
                dp[0] = 0
                cur_comb = None
                for comb in combs:
                    comb = (1,) + comb
                    comb = tuple(list(set(comb)))
                    if comb not in cache:
                        counter = 1
                        while True:
                            for c in comb:
                                if c <= counter:
                                    dp[counter] = min(dp[counter] if counter in dp else float('inf'),
                                                      dp[counter - c] + 1)
                            if dp[counter] <= h:
                                loc_max = max(loc_max, counter)
                            else:
                                break
                            counter += 1
                        cur_comb = comb
                        cache[comb] = loc_max
                    else:
                        cur_comb = comb
                        loc_max = cache[comb]

                if loc_max > _max:
                    _max = cache[cur_comb]
                    max_comb = cur_comb
                else:
                    break
                n += 1

    print(f"{' '.join(map(str, max_comb))} -> {_max}")

import  collections


# def solve():
#     loc_max = 0
#     cur_comb = None
#     _max = 0
#     s = set()
#     is_max_set = False
#     def backtrack(comb, i, k, h):
#         nonlocal loc_max, cur_comb, _max, is_max_set
#         if len(comb) == k:
#             t = tuple(comb)
#             if t in s:
#                 print('duplicate')
#                 return
#             s.add(t)
#             #print(comb)
#             d = collections.defaultdict(int)
#             #d = {0:0, 1: 1}
#             d[0] = 0
#             target = 1
#             while True:
#                 for c in comb:
#                     if c <= target:
#                         d[target] = min(float('inf') if target not in d else d[target], d[target - c] + 1)
#                 if d[target] > h:
#                     break
#                 target += 1
#             if target > loc_max:
#                 loc_max = target
#                 cur_comb = comb[:]
#                 #return True
#             else:
#                 if not is_max_set:
#                     _max = loc_max + 1
#                     is_max_set = True
#             return
#
#         if i == 1:
#             comb.append(i)
#             backtrack(comb, i + 1, k, h)
#         else:
#             while i < _max or _max == 0:
#                 comb.append(i)
#                 backtrack(comb, i + 1, k, h)
#                 comb.pop()
#                 # if backtrack(comb, i + 1, k, h):
#                 #     comb.pop()
#                 # else:
#                 #     return False
#                 i += 1
#
#     while True:
#         h, k = map(int, next(tests).split())
#         if h == 0 and k == 0:
#             break
#
#         # if h == 1:
#         #     print(f"{' '.join(map(str, range(1, k +1)))} -> {loc_max - 1}")
#         #     continue
#
#         # if k == 1:
#         #     print(h)
#         #     continue
#         backtrack([], 1, k, h)
#
#     print(f"{' '.join(map(str, cur_comb))} -> {loc_max-1}")

tests = iter(["5 5", "0 0"])
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
        #h, k = next(tests).split()
        h, k = input().split()
        if not h or not k:
            continue
        h, k = int(h), int(k)
        if h == 0 and k == 0:
            break

        if h + k > 9:
            continue
        if k == 0:
            print(f"0 -> 0")
            continue
        backtrack([], 1, k, h)

        print(f"{' '.join(map(str, cur_comb))} -> {loc_max-1}")


if __name__ == '__main__':
    solve()
    # backtrack([], 1, 3, 5)
    # print(len(res))
    # main()


    # 5 4
    # 4 5
    # 6 3
    # 8 2
    # 4 4
    # 5 5
    # 0 0

      #1  4 12 21 ->  71
      #1  3 11 15 32 ->  70
      #1  7 12 ->  52
      #1  5 ->  28
      #1  3 11 18 ->  44
      #1  4  9 31 51 -> 126