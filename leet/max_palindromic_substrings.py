

def solution2(s):
    r = 0 # stores the center of the longest palindromic substring until now
    c = 0 # stores the right boundary of the longest palindromic substring until now
    P = [0] * (2 * len(s)+1)
    # this makes length of the string to be odd even if initially the length of s was even
    s = '#' + '#'.join(s) + '#'

    for i in range(0, len(s)):
        # get mirror index of i
        mirror = 2 * c - i

        #see if the mirror of i is expanding beyond the left boundary of current longest palindrome at center c
        #if it is, then take r - i as P[i]
        #else take P[mirror] as P[i]
        if i < r:
            P[i] = min(r - i, P[mirror])

        # expand at i
        a = i + (1 + P[i])
        b = i - (1 + P[i])


        while a < len(s) and b >= 0 and s[a] == s[b]:
            b -= 1
            a += 1
            P[i] += 1

        #check if the expanded palindrome at i is expanding beyond the right boundary of current longest palindrome at center c
        #if it is, the new center is i
        if i + P[i] > r:
            c = i
            r = i + P[i]
    return P



def left():
    print('left')
    return False

def right():
    print('right')
    return True


if __name__ == '__main__':
    a = []
    if left() and right():
        print(8)
    p = solution2("aabcba")
    print(p)


