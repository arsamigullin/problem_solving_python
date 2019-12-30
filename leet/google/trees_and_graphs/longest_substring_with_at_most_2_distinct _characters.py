# Algo
# 1. We maintain two pointers i - to point to the current char
# j - to point to the new position since which the count of distinct chars is less than 2
# 2. Iterate over string and index of current char in dict
# NOTE: instead of count we store index of the char
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        max_len, i, j = 0, 0, 0
        d = {}
        while i < len(s):
            d[s[i]]=i
            if len(d) > 2:
                rem_idx = min(d.values())
                d.pop(s[rem_idx], None)
                j = rem_idx + 1
            max_len = max(max_len, i - j + 1)
            i+=1
        return max_len