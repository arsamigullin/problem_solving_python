# this problem
#https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1
        cnt = float('inf')
        for c in 'balon':
            if c in d:
                count = d[c] // 2 if c in ('o', 'l') else d[c]
                cnt = min(cnt, count)
            else:
                return 0
        return cnt


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('a'), text.count('b'), text.count('l') // 2, text.count('o') // 2, text.count('n'))