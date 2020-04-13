import collections
class SolutionMy:
    def firstUniqChar(self, s: str) -> int:
        c = collections.OrderedDict()
        for ch in s:
            c[ch] = c.get(ch, 0) + 1
        single = ' '
        for k, v in c.items():
            if v == 1:
                single = k
                break
        return s.find(single)


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # as we know Counter will add numbers without order
        count = collections.Counter(s)

        # therefore we will use the string that will provide the order for us
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1