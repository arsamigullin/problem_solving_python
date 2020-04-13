import collections
from typing import List

# this problem https://leetcode.com/problems/group-shifted-strings/
# 249. Group Shifted Strings

class SolutionMy:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        d = collections.defaultdict(list)
        for s in strings:
            dif = list()
            for i in range(1, len(s)):
                ch1 = ord(s[i]) - ord('a')
                ch2 = ord(s[i - 1]) - ord('a')
                # why do we need this
                # consider an example
                # [az, ba]
                # the gap to move toward successive char can be more that one
                # in this example the gap for both is 25. abcdef...z 25 and bcdefg...za
                # to correctly calculate the gap size we must add 26 in case of the next char is less that previous
                if ch1 < ch2:
                    ch1 += 26
                dif.append(ch1 - ch2)
            d[tuple(dif)].append(s)
        return d.values()


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        # why this works???
        # consider example [az, ba]
        # for az we have: ord(a) - ord(a) = 0 and ord(z) - ord(a) = 122 - 97 = 25
        # for ba we have: ord(b) - ord(b) = 0 and ord(a) - ord(b) = 97 - 98 = -1
        # The key thing here is %26. 25%26 = 25 and -1%26= 25
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += [s]

        return map(sorted, groups.values())

if __name__ == '__main__':
    s = Solution()
    s.groupStrings(["az","ba"])