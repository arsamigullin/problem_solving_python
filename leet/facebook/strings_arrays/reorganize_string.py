import collections

class Solution:
    '''
    if no elements in string with count > than len(S)//2
    then it is possible

    we will do an injection
    let's consider this string
    aaaabbb

    we create an empty array of length S
    res = [a, , a, , a, , a] # res[0::2] = cs[:l]
    res = [a,b,a,b,a,b,a] # res[1::2] = cs[l:]

    '''
    def reorganizeString(self, S: str) -> str:
        c = collections.Counter(S)
        l = len(S) // 2 + len(S) % 2
        if c.most_common(1)[0][1] > l:
            return ""

        cs = sorted(c.elements(), key=lambda k: c[k] * -1) # -1 does reverse
        res = [''] * len(S)
        res[0::2] = cs[:l]
        res[1::2] = cs[l:]
        return ''.join(res)