def solution(s):
    d = dict()
    res = 0
    count = 0
    i = 0
    while i < len(s):
        if s[i] in d:
             next_index = d[s[i]] + 1
             d[s[i]] = i
             i = next_index
             d = dict()
             count = 0
        else:
            d[s[i]] = i
            count+=1
            i+=1
        res = max(res, count)

    return res

def lengthOfLongestSubstring(s):
    dct = {}
    max_so_far = curr_max = start = 0
    for index, i in enumerate(s):
        if i in dct and dct[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dct[i]
            start = dct[i] + 1
        else:
            curr_max += 1
        dct[i] = index
    return max(max_so_far, curr_max)

def slidingWindowSolution(s):
    # i and j will compose window
    # Once the char is found in the map we will narrow window increasing i
    n = len(s)
    ans = j = i = 0
    map = dict()
    while j<n:
        if s[j] in map:
            i = max(map[s[j]], i)
        ans = max(ans, j-i+1)
        map[s[j]] = j + 1
        j+=1
    return ans

if __name__ == "__main__":
    slidingWindowSolution('abcabcbb')
    lengthOfLongestSubstring('abcabcbb')
    solution('abcabcbb')
