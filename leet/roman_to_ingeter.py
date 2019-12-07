def romanToInt(s):
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    sub = ['I', 'X', 'C']
    total = 0
    i = 0
    while i<=len(s):
        if s[i] in sub:
            if i+1 >= len(s):
                total += d[s[i]]
            else:
                if s[i] + s[i + 1] in d:
                    total += d[s[i] + s[i + 1]]
                    i = i + 2
                    continue
                else:
                    total += d[s[i]]
        else:
            total += d[s[i]]
            
        i += 1

    return total

def romanToIntRevisited(s):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'XL': 40, 'CD': 400, 'IX': 9,
         'XC': 90, 'CM': 900}
    i = 0
    num = 0
    n = len(s)
    while i < n:
        if s[i] in ['I', 'X', 'C']:
            if i < n - 1:
                r = s[i] + s[i + 1]
                if r in d:
                    num += d[r]
                    i += 2
                    continue
        num += d[s[i]]
        i += 1
    return num

if __name__ == '__main__':
    print(romanToInt("III"))