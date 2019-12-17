# https://leetcode.com/problems/minimum-window-substring/
# we are using here sliding window technique
# i and j are composing window
# we starting from j and moving it until all the letters of t is covered
# at the beginning we are fixing total items of t
# On each iteration we checking if the count of letters from s (int_tot) is equal to total.
import collections


def solution(s, t):
    if len(s) < len(t):
        return ""
    dt = {}
    total = 0
    int_tot = len(t)
    for c in t:
        if c in dt:
            dt[c] += 1
        else:
            dt[c] = 1

    i, j = 0, 0
    needed = {}  #to track letters from s and compare them with dt to maintain the same count for each letter
    res = ""
    while i < len(s):

        while int_tot != total and j < len(s):
            ltc = s[j] # letter to check from s
            if ltc in dt:
                if ltc in needed:
                    needed[ltc] += 1
                else:
                    needed[ltc] = 1
                # we increase count only if it is less or equal in dt. But real count of letters is maintained right above
                # no need to increase int_tot if we reached the same count of ltc in dt
                if needed[ltc] <= dt[ltc]:
                    int_tot += 1
            j += 1

        if int_tot == total:
            if ltc in dt:
                needed[ltc] -= 1
                # we decreasing int_total only when it is less than count of the same letter in dt
                if needed[ltc] < dt[ltc]:
                    int_tot -= 1
                # redefining result
                if res == "" or j - i < len(res):
                    res = s[i: j]
            i += 1
        else:
            break
    return res

def minWindow(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]

if __name__ == "__main__":
    print(solution("ab", "a"))
    #print(solution("a", "b"))
    #print(solution("ADOBECODEBANC", "ABC"))
