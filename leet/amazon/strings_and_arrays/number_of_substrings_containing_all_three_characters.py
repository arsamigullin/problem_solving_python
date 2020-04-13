# this problem
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

# exact problem
# subarrays_with_K_different_integers.py - See explanation here
# https://leetcode.com/problems/subarrays-with-k-different-integers/

import  collections

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = collections.defaultdict(int)
        res, left, j = 0, 0, 0
        for i in range(len(s)):
            d[s[i]] += 1

            if len(d) == 3:
                while d[s[left]] > 1:
                    d[s[left]] -= 1
                    left += 1
                res += left - j + 1
        return res