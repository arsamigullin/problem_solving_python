# this problem
# https://leetcode.com/problems/valid-word-abbreviation/

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        curr, dig = 0, '0'
        for x in abbr:
            if x.isdigit():
                if x == '0' and not int(dig):
                    return False
                dig += x
            else:
                if dig:
                    curr += int(dig)
                if curr >= len(word):
                    return False
                if x != word[curr]:
                    return False
                curr += 1
                dig = '0'
        curr += int(dig)
        return curr == len(word)