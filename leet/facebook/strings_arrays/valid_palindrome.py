# 125 https://leetcode.com/problems/valid-palindrome/
def solution(s):
    i, j = 0, len(s)-1
    while i!=j:
        if not s[i].isnumeric() and not s[i].isalpha():
            i+=1
            continue
        if not s[j].isnumeric() and not s[j].isalpha():
            j-=1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True


import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-zA-Z0-9]", s)).lower()
        return s == s[::-1]